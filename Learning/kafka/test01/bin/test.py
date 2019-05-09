#coding=utf-8

import time
import logging
import sys
import json
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from kafka import TopicPartition


kafka_mgr = {
    "broker" : '9.24.131.208',
    "port" : 9092,
    "topic":"212_23_oc_reverse_ping_detector_v2"
}


class kfkConsumer(object):

    # consumer = None

    def __init__(self, broker, kafkaPort, kafkaTopic=''):
        self._broker = broker
        self._kafkaPort = kafkaPort
        self._kafkaTopic = kafkaTopic

    def __str__(self):
        print("--------------------------------")
        print("kafka-consumer params ...")
        print("[KAFKA-BROKER]:%s" %self._broker)
        print("[KAFKA-PORT]:%s" %self._kafkaPort)
        print("[KAFKA-TOPIC]:%s" %self._kafkaTopic)
        print("--------------------------------")

    def registerConsumer(self):
        try:
            consumer = KafkaConsumer(
                bootstrap_servers=[self._broker+':'+self._kafkaPort],
                auto_offset_reset='earliest')
        except KafkaError as e:
            logging.info(e)
        return consumer

    def consumerMsg(self, topic, partition=0):
        try:
            v_consumer = self.registerConsumer()
            v_consumer.assign([TopicPartition(topic,partition)])
            # self.registerConsumer.subscribe([self._kafkaTopic])
            for message in v_consumer:
                # message value and key are raw bytes -- decode if necessary!
                # e.g., for unicode: `message.value.decode('utf-8')
                print("%s:%d:%d: msg=%s" % (message.topic, message.partition,
                                                        message.offset, message.value.decode('utf-8')))
        except KafkaError as e:
            logging.info(e)

if __name__ == '__main__':
    consumer = kfkConsumer(kafka_mgr["broker"], kafka_mgr["port"], kafka_mgr["topic"])
    consumer.consumerMsg()