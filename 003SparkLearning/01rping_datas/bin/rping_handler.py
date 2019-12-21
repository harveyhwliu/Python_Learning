#!/usr/bin/python
#-*-coding: utf-8-*-
import streaming_datask_lib as sdlib
import time
import random
import MySQLdb
import traceback
import re
import json
import struct
import snappy

def analysis_line_content(line):
    """
    获取kafka中的 每一行 数据
    :param line:
    :return:
    """
    _t_module_mark = "212_8_oc_reverse_ping_detector"
    try:
        _bytes_content = bytes(line)
        agent_ip, agent_time, agengt_seq, module_mark_size = struct.unpack('>4I', _bytes_content[0:16]) # 前16个字节都是网络序的 unsigned int
        unpack_format = '%ds%ds' % (module_mark_size,len(_bytes_content)-16-module_mark_size)           # 紧接着的第一个字段是软件标识，最后一个字段是snappy压缩后的文本内容
        module_mark,content = struct.unpack(unpack_format,_bytes_content[16:])
        if module_mark != _t_module_mark:
            errorMsg = "---coffee---,error for get module_mark [%s != %s]"%(module_mark,_t_module_mark)
            print errorMsg
            return None
        agent_time = agent_time/60*60   # 泛化为分钟粒度,规避业务逻辑处理上的指标字段缺失的问题
        content = snappy.uncompress(content)
        _content = map(lambda x:"%d#%s"%(agent_time,x),filter(lambda y:y,content.split("\n")))
        return "\n".join(_content)                                        #文本内容通过snappy解压缩后得到)
    except Exception as e:
        errorMsg = "--coffee--,error for analysis_line_content [%s],%s | %s"%(str(line),str(e),traceback.format_exc())
        print errorMsg
        return None

def get_targets_data(line):
    """
    抽取指标数据
    212_8_oc_reverse_ping_detector#oc_name=compare_海口电信凤翔路OC5-30G-N|oc_prov=海南|oc_isp=电信|oc_bu=none|target_area=青海电信#loss##src_ip=172.20.57.146#22
    links:
        oc_name=compare_海口电信凤翔路OC5-30G-N|oc_prov=海南|oc_isp=电信|oc_bu=none|target_area=青海电信
    :param line:
    :return:
    """
    try:
        agent_timestamp,_,links,target,src_ip,_,target_value = line.split("#")  #agent上报时间,标识，维度，指标，src_ip,指标值
        agent_timedate = time.strftime('%Y%m%d',time.localtime(int(agent_timestamp)))
        if not links.strip():
            return (None,None)
        key = "time_stamp=%s|time_date=%s|%s"%(agent_timestamp,agent_timedate,links)
        value = "%s=%s"%(target,target_value)
        return (key, value)
    except Exception as e:
        errorMsg = "--coffee--,error for get_targets_data,[%s] |[%s] %s"%(str(line),str(e),traceback.format_exc())
        print errorMsg
        return (None,None)

def usr_define_func(rdd,isp_info,prov_info,idc_info):
    """
        消费kafka数据，并生成结果数据，完成入库动作
    temp:
        timestamp=1576740112|oc_name=compare_宁波电信镇海OC3-30G-V|oc_prov=浙江|oc_isp=电信|oc_bu=none|target_area=安徽电信
        loss=16|delay=16|detect_count=320|detect_fail_count=180|lost_rate_sigma=49
    :param rdd:
    :param isp_info:
    :param prov_info:
    :param idc_info:
    :return:
    """
    start_time = time.time()
    result = rdd.filter(lambda line: line is not None and line[1] != '' and line[1] is not None)\
        .map(lambda line: line[1]) \
        .map(lambda line: analysis_line_content(line)) \
        .filter(lambda line: line is not None) \
        .flatMap(lambda line: line.split("\n")) \
        .filter(lambda line: line is not None) \
        .map(lambda line:get_targets_data(line)) \
        .filter(lambda line: line[0] is not None and line[1] is not None) \
        .reduceByKey(lambda x, y: "%s|%s"%(x,y))
    errorMsg_l = []  # 处理出现了失败的信息 list
    mysql_res = {}  # 待插入的mysql表名 list
    try:
        mysql_datas=result.collect()    # 待处理的上报数据
        for line in mysql_datas:
            try:
                links_d = dict(map(lambda x:x.split("="),line[0].split("|")))
                values_d = dict(map(lambda x:x.split("="),line[1].split("|")))
                # 核心指标数据缺失的，一律忽略
                if not links_d.has_key("oc_name") or not links_d.has_key("oc_isp") or not links_d.has_key("target_area") \
                    or not links_d.has_key("oc_isp") or not links_d.has_key("time_stamp") or not values_d.has_key("loss") \
                    or not values_d.has_key("delay"):
                    continue
                if idc_info.has_key(links_d["oc_name"]):
                    s_idc_id = idc_info[links_d["oc_name"]]["oc_id"]
                    s_idc_isp_id = idc_info[links_d["oc_name"]]["oc_isp_id"]
                    s_idc_prov_id = idc_info[links_d["oc_name"]]["oc_prov_id"]
                    user_prov,user_isp = [str(x) for x in links_d["target_area"].split(links_d["oc_isp"])]
                    c_idc_isp_id = isp_info[user_isp] if isp_info.has_key(user_isp) else -1
                    c_idc_prov_id = prov_info[user_prov] if prov_info.has_key(user_prov) else -1
                    delay = str(values_d["delay"]) if values_d.has_key("delay") else "-1"
                    loss = str(values_d["loss"]) if values_d.has_key("loss") else "-1"
                    detect_fail_count = str(values_d["detect_fail_count"]) if values_d.has_key("detect_fail_count") else "0"
                    detect_count = str(values_d["detect_count"]) if values_d.has_key("detect_count") else "0"
                    lost_rate_sigma = str(values_d["lost_rate_sigma"]) if values_d.has_key("lost_rate_sigma") else "0"
                    _sql="(%s,%d,%d,%d,%d,%d,%s,%s,%s,%s,%s,%d)"%(links_d["time_stamp"],c_idc_isp_id,c_idc_prov_id,s_idc_id,s_idc_isp_id,s_idc_prov_id,loss,delay,detect_fail_count,detect_count,lost_rate_sigma,3)
                    try:
                        mysql_res[links_d["time_date"]].append(_sql)
                    except:
                        mysql_res[links_d["time_date"]] = []
                        mysql_res[links_d["time_date"]].append(_sql)
                else:
                    continue
            except Exception as e:
                if str(e) not in errorMsg_l:
                    errorMsg_l.append(str(e))
                    errorMsg_l.append(str(line))
                    errorMsg_l.append(traceback.format_exc())
    except Exception, e:
        errorMsg = "---coffee----,get rping datas error ,for [%s],%s"%(str(e),traceback.format_exc())
        print errorMsg
    if errorMsg_l:
        print "---coffee----,get rping datas error ,for %s"%("\n".join(errorMsg_l))
    _res_mysql_datas = {}
    for rping_datas_date,values in mysql_res.iteritems():
        batch_num = 50000       # 每次 插入  batch_num 数据
        table_name = "rping_%s"%(rping_datas_date)
        _res_mysql_datas[table_name] = []
        while True:
            if len(values) >= batch_num:
                _res_mysql_datas[table_name].append(handler_mysql_datas(table_name, values[0:batch_num]))
                values = values[batch_num:]
            elif values:
                _res_mysql_datas[table_name].append(handler_mysql_datas(table_name, values))
                values = []
            else:
                break
    if _res_mysql_datas and  False in reduce(lambda x, y: list(set(x + y)), _res_mysql_datas.values()):
        print "---coffee----,save rping datas into Mysql failed ，please check details log"


def insert_mysql_db(sql):
    """
    数据入库,每次直接重试 _max_retries_count 次
    :param sql:
    :return:
    """
    _success_status = False
    _max_retries_count = 2      # 设置最大重试次数
    _conn_retries_count = 0     # 初始重试次数
    try:
        conn = MySQLdb.connect("*.*.*.*", "name", "passwd", "databases_name", port=232,charset='utf8')
        cursor = conn.cursor()
        while not _success_status:
            try:
                if _conn_retries_count <= _max_retries_count:
                    cursor.execute(sql)
                    conn.commit()
                    cursor.close()
                    _success_status = True
                    return _success_status
            except Exception as e:
                _conn_retries_count += 1
                if _conn_retries_count <= _max_retries_count:
                    _success_status = False
                time.sleep(1)
                errorMsg = "--- coffee -- ,error for retry:[%d | %d] times ,[%s],[%s]:%s"%(_conn_retries_count,_max_retries_count,sql,str(e),traceback.format_exc())
                print errorMsg
    except Exception as e:
        errorMsg = "--- coffee -- ,connect mysql failed for [%s] : %s" % (str(e), traceback.format_exc())
        print errorMsg
    return _success_status

def handler_mysql_datas(table_name,mysql_datas):
    """
    数据入库,重试 retry_cnt组
    :param table_name:
    :return:
    """
    sql = "insert into " + table_name + " (`time_stamp`, `c_idc_isp_id`,`c_idc_prov_id`,`s_idc_id`,`s_idc_isp_id`,`s_idc_prov_id`,`loss`,`delay`,`failed_cnt`,`total_cnt`,`lost_rate_sigma`,`datas_source_type`) values "
    sql += ",".join(mysql_datas)
    sql += " ON DUPLICATE KEY UPDATE `loss` = VALUES(`loss`),`delay` = VALUES(`delay`),`failed_cnt` = VALUES(`failed_cnt`),`total_cnt` =  VALUES(`total_cnt`),`lost_rate_sigma` = VALUES(`lost_rate_sigma`);"
    retry_cnt = 3
    while retry_cnt > 0:
        ret = insert_mysql_db(sql)
        if ret:
            retry_cnt = 1
            break
        else:
            time.sleep(2)
            retry_cnt -= 1
    if retry_cnt > 0:
        return True
    else:
        return False

def init_environment(datask):
    """
    初始化环境，返回私有私有信息等
    :return:
    """
    isp_info_path = r"cos4n://tegapd1006/txCloudVideo_v5/coffee_aiops/200076/isp_info.ini"
    isp_container = {}
    prov_info_path = r"cos4n://tegapd1006/txCloudVideo_v5/coffee_aiops/200076/prov_info.ini"
    prov_container = {}
    idc_info_path = "cos4n://tegapd1006/txCloudVideo_v5/coffee_aiops/200076/oc_name_to_id.ini"
    idc_container = {}
    file_pipe = datask.get_data_pipe(sdlib.PipeType.FILE)
    #运营商 映射关系
    rdd_tmp = file_pipe.load_file(isp_info_path, False, False).map(lambda line: [str(s) for s in line.split("\t")]).\
        map(lambda x: (x[0], int(x[1]))).collect()
    for items in rdd_tmp:
        isp_container[items[0]] = int(items[1])
    #省份 映射关系
    rdd_tmp = file_pipe.load_file(prov_info_path, False, False).map(lambda line: [str(s) for s in line.split("\t")]).\
        map(lambda x: (x[0], int(x[1]))).collect()
    for items in rdd_tmp:
        prov_container[items[0]] = int(items[1])
    #机房名映射关系
    rdd_tmp = file_pipe.load_file(idc_info_path, False, False).map(lambda line: [str(s) for s in line.split("\t")]).\
        map(lambda x: (x[0], [int(x[1]), int(x[2]), int(x[3])])).collect()
    for items in rdd_tmp:
        idc_container[items[0]] = dict({"oc_id":items[1][0],"oc_isp_id":items[1][2],"oc_prov_id":items[1][1]})
    return isp_container,prov_container,idc_container


def datask_run(datask, argv = []):
    """
    spark - python 入口函数
    :param datask:
    :param argv:
    :return:
    """
    topic = '212_8_oc_reverse_ping_detector'
    dstream = datask.get_dstream(topic)
    print 'datask.get_dstream success'
    isp_info,prov_info,idc_info = init_environment(datask)
    dstream.foreachRDD(lambda rdd: usr_define_func(rdd,isp_info,prov_info,idc_info))
