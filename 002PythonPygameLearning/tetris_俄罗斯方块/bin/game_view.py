#-*- coding:utf8 -*-


import pygame
from random import choice
from game_meta import TetrisMeta

class TetrisGameView(object):
    """
    俄罗斯方块游戏 视图类
    """
    def __init__(self,params):
        #游戏中其他全局配置
        self.__bg_color = params["bg_color"]                    #背景颜色
        self.__windows_margin_top = params["margin_top"]        #游戏窗口，  距离上的间距
        self.__windows_margin_bottom = params["margin_left"]    #游戏窗口，  距离下的间距
        self.__windows_margin_left = params["margin_right"]     #游戏窗口，  距离左的间距
        self.__windows_margin_right = params["margin_bottom"]   #游戏窗口，  距离右的间距
        #游戏分区 - 最小显示的单位
        self.__block_size = params["block_size"]                #游戏视图区域的最小单位
        #边界线
        self.__border_color = params["border_color"]            #游戏视图各个功能区的边界线颜色
        self.__border_width = params["border_width"]            #边界线线宽
        #游戏区
        self.__game_show_area_width = params["game_show_area_width"]
        self.__game_show_area_height = params["game_show_area_height"]
        #游戏过程中数据展示区
        self.__game_datas_area_width = params["game_datas_area_width"]

        #游戏主窗口  主面板
        self.__game_screen = params["screen"]
        self.__game_all_width = params["game_all_width"]        #游戏窗口的宽
        self.__game_all_height = params["game_all_height"]      #游戏窗口的长

        #绘制游戏背景
        self.__game_screen.blit(self.construct_bg_image(self.__game_screen.get_size()),(0,0))#第一个参数为一个Surface对象，第二个为左上角位置

        #俄罗斯方块的基础操作等
        self.__tetris_meta = TetrisMeta()
        self.__based_tetris_shape_l = self.__tetris_meta.get_based_tetris_shape()

    def construct_bg_image(self,size):
        """
        绘制背景
        :param size:
        :return:
        """
        surf = pygame.Surface(size)

        boxsize = 8         #每个显示块的大小
        bordersize = 1
        vals = '0123456789' # only the lower values, for darker colors and greater fear
        arr = pygame.PixelArray(surf)
        for x in range(0, len(arr), boxsize):
            for y in range(0, len(arr[x]), boxsize):
                color = int(''.join([choice(vals) + choice(vals) for _ in range(3)]),16)
                # color = int(''.join([choice(vals) + choice(vals)+choice(vals) for _ in range(3)]))
                for LX in range(x, x+(boxsize - bordersize)):
                    for LY in range(y, y+(boxsize - bordersize)):
                        if LX < len(arr) and LY < len(arr[x]):
                            arr[LX][LY] = color
        del arr     #告诉pygame ，已经绘制好了像素位置
        return surf


    def handler(self):
        """
        游戏视图类 具体操作包括：
        :return:
        """

        #1  绘制游戏背景  如果想要动态效果，放到这里

        #2 游戏分区

        game_show_area = pygame.Surface((self.__game_show_area_width*self.__block_size+self.__border_width*2,
                                        self.__game_show_area_height*self.__block_size+self.__border_width*2))
        game_show_area.fill(self.__border_color)
        self.__game_screen.blit(game_show_area, (self.__windows_margin_left,self.__windows_margin_top))

        #3 游戏视图更新
        self.update_view()
        
    #
    # def main(self, screen):
    #     clock = pygame.time.Clock()
    #
    #     self.matris = Matris()
    #
    #     self.update_view()
    #
    #     while True:
    #         try:
    #             timepassed = clock.tick(50)
    #             if self.matris.update((timepassed / 1000.) if not self.matris.paused else 0):
    #                 self.update_view()
    #         except GameOver:
    #             return



    def update_view(self):
        """
        更新游戏内容
        :return:
        """
        # if not self.matris.paused:
        if 1:
            #1 绘制下一个俄罗斯方块的图形
            center_width = self.__game_all_width-(self.__game_all_width-(self.__windows_margin_left+self.__game_show_area_width*self.__block_size+self.__border_width*2))/2

            # nextts = self.next_tetromino_surf(self.matris.surface_of_next_tetromino)
            # screen.blit(nextts, nextts.get_rect(top=MATRIS_OFFSET, centerx=tricky_centerx))
            
            #2 绘制游戏得分情况
            game_score = self.game_datas_details()
            print game_score
            self.__game_screen.blit(game_score, game_score.get_rect(bottom=self.__game_show_area_height-self.__windows_margin_top, centerx=center_width))

            # self.matris.draw_surface()
        pygame.display.flip()


    def game_datas_details(self):
        """
        展示  游戏过程中的数据情况
        :return:
        """
        textcolor = (255, 255, 255)
        font = pygame.font.Font(None, 30)       #创建字体对象
        score_datas_width = (self.__game_all_width-(self.__windows_margin_left+self.__game_show_area_width*self.__block_size+self.__border_width*2))\
                            - self.__windows_margin_left

        def renderpair(text, val):
            """
            绘制 游戏数据信息
            :param text:  游戏Key 属性
            :param val:   游戏Val 字段
            :return:
            """
            text = font.render(text, True, textcolor)      #在一个新 Surface 对象上绘制文本,仅支持渲染一行文本
            val = font.render(str(val), True, textcolor)

            surf = pygame.Surface((score_datas_width, text.get_rect().height + self.__border_width*2), pygame.SRCALPHA, 32)

            surf.blit(text, text.get_rect(top=self.__border_width+self.__windows_margin_top, left=self.__border_width+self.__windows_margin_left))
            surf.blit(val, val.get_rect(top=self.__border_width+self.__windows_margin_top, right=score_datas_width-(self.__border_width+self.__windows_margin_right)))
            return surf

        scoresurf = renderpair("Score", 0)
        levelsurf = renderpair("Level", 0)
        linessurf = renderpair("Lines", 0)
        combosurf = renderpair("Combo", "x{}".format("100"))

        score_datas_height = 20 + (levelsurf.get_rect().height +
                       scoresurf.get_rect().height +
                       linessurf.get_rect().height +
                       combosurf.get_rect().height )

        area = pygame.Surface((score_datas_width, score_datas_height))
        area.fill(self.__border_color)
        area.fill(self.__bg_color, pygame.Rect(self.__border_width, self.__border_width, score_datas_width-self.__border_width*2, score_datas_height-self.__border_width*2))

        area.blit(levelsurf, (0,0))
        area.blit(scoresurf, (0, levelsurf.get_rect().height))
        area.blit(linessurf, (0, levelsurf.get_rect().height + scoresurf.get_rect().height))
        area.blit(combosurf, (0, levelsurf.get_rect().height + scoresurf.get_rect().height + linessurf.get_rect().height))

        return area
    """
    def next_tetromino_surf(self, tetromino_surf):
        area = Surface((BLOCKSIZE*5, BLOCKSIZE*5))
        area.fill(BORDERCOLOR)
        area.fill(BGCOLOR, Rect(BORDERWIDTH, BORDERWIDTH, BLOCKSIZE*5-BORDERWIDTH*2, BLOCKSIZE*5-BORDERWIDTH*2))

        areasize = area.get_size()[0]
        tetromino_surf_size = tetromino_surf.get_size()[0]
        # ^^ I'm assuming width and height are the same

        center = areasize/2 - tetromino_surf_size/2
        area.blit(tetromino_surf, (center, center))

        return area
    
    """
