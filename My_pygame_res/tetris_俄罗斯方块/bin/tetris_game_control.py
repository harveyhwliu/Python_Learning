#!/usr/local/bin/python
#-*- coding:utf8 -*-
import pygame
from game_view import TetrisGameView

class TetrisGameController(object):
    """
    俄罗斯方块游戏控制类
    负责游戏的产生、结束等
    """
    def __init__(self):
        """
        全局资源配置
        """
        #游戏中其他全局配置
        self.__bg_color = (15,15,20)                 #背景颜色
        self.__game_title = u"俄罗斯方块游戏"
        self.__windows_margin_top = 20               #游戏窗口，  距离上的间距
        self.__windows_margin_bottom = 20            #游戏窗口，  距离下的间距
        self.__windows_margin_left = 20              #游戏窗口，  距离左的间距
        self.__windows_margin_right = 20             #游戏窗口，  距离右的间距
        self.__game_clock = pygame.time.Clock()           #游戏时钟
        #游戏分区 - 最小显示的单位
        self.__block_size = 30                       #游戏视图区域的最小单位
        #边界线
        self.__border_color = (140,140,140)          #游戏视图各个功能区的边界线颜色
        self.__border_width = 10                     #边界线线宽
        #游戏区
        self.__game_show_area_width = 18
        self.__game_show_area_height = 25
        #游戏过程中数据展示区
        self.__game_datas_area_width = 350

        #整个游戏窗口的大小  游戏区对应大小+边界线宽
        self.__all_width = self.__game_show_area_width*self.__block_size + self.__border_width*4 \
                           + self.__game_datas_area_width +self.__windows_margin_left + self.__windows_margin_right
        self.__all_height= self.__game_show_area_height*self.__block_size + self.__border_width*2 + self.__windows_margin_top \
                           + self.__windows_margin_bottom

    def get_game_windows_size(self):
        """
        获取整个游戏窗口的大小
        :return:
        """
        return (self.__all_width,self.__all_height)

    def get_game_title(self):
        """
        获取游戏标题
        :return:
        """
        return self.__game_title

    def get_game_clock(self):
        """
        获取游戏时钟
        :return:
        """
        return self.__game_clock

    def get_bg_color(self):
        """
        获取背景颜色
        :return:
        """
        return self.__bg_color

    def get_game_windows_margin(self):
        """
        获取游戏窗口的 margin 信息
        :return:按照 上、下、左、右 返回
        """
        return (self.__windows_margin_top,self.__windows_margin_bottom,self.__windows_margin_left,self.__windows_margin_right)

    def get_game_view_unit(self):
        """
        游戏视图区域的最小单位
        :return:
        """
        return self.__block_size

    def get_border_info(self):
        """
        获取游戏区别的  边界线属性
        :return:
        """
        return (self.__border_width,self.__border_color)

    def get_game_show_area_info(self):
        """
        获取游戏区的信息
        :return:
        """
        return (self.__game_show_area_width,self.__game_show_area_height)

    def get_game_datas_area_info(self):
        """
        获取游戏过程中数据展示区  的信息
        :return:
        """
        return self.__game_show_area_width

    def get_all_config_info(self):
        """
        获取全局的配置信息
        :return:
        """
        params = {"bg_color":self.__bg_color,"margin_top":self.__windows_margin_top,"margin_left":self.__windows_margin_left,
                  "margin_right":self.__windows_margin_right,"margin_bottom":self.__windows_margin_bottom,"block_size":self.__block_size,
                  "border_color":self.__border_color,"border_width":self.__border_width,"game_show_area_width":self.__game_show_area_width,
                  "game_show_area_height":self.__game_show_area_height,"game_datas_area_width":self.__game_datas_area_width,
                  "game_all_width":self.__all_width,"game_all_height":self.__all_height}

        return params

    def play_game(self):

        #游戏框架搭建
        pygame.init()
        game_windows_size = self.get_game_windows_size()
        self.game_screen = pygame.display.set_mode(game_windows_size)   #游戏主面板
        pygame.display.set_caption(self.get_game_title())
        # clock = self.get_game_clock()

        #游戏视图类相关操作
        params = self.get_all_config_info()
        params["screen"] = self.game_screen
        game_model = TetrisGameView(params)

        #事件循环
        while 1:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            game_model.handler()

            # clock.tick(10)
            #
            # #显示背景
            # self.game_screen.blit(nightmare, (0,0))
            pygame.display.flip()


if __name__ == '__main__':
    tetris_helper = TetrisGameController()
    tetris_helper.play_game()
