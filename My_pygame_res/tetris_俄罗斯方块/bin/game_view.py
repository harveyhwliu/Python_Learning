#-*- coding:utf8 -*-


import pygame
from common_method import ICommonMethod


class TetrisGameView(ICommonMethod):
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

        #1  绘制游戏背景
        self.__game_screen.blit(self.construct_bg_image(self.__game_screen.get_size()),(0,0))#第一个参数为一个Surface对象，第二个为左上角位置

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

    #
    # def main(self, screen):
    #     clock = pygame.time.Clock()
    #
    #     self.matris = Matris()
    #
    #     self.redraw()
    #
    #     while True:
    #         try:
    #             timepassed = clock.tick(50)
    #             if self.matris.update((timepassed / 1000.) if not self.matris.paused else 0):
    #                 self.redraw()
    #         except GameOver:
    #             return

    """

    def redraw(self):
        if not self.matris.paused:
            tricky_centerx = WIDTH-(WIDTH-(MATRIS_OFFSET+BLOCKSIZE*MATRIX_WIDTH+BORDERWIDTH*2))/2

            nextts = self.next_tetromino_surf(self.matris.surface_of_next_tetromino)
            screen.blit(nextts, nextts.get_rect(top=MATRIS_OFFSET, centerx=tricky_centerx))

            infos = self.info_surf()
            screen.blit(infos, infos.get_rect(bottom=HEIGHT-MATRIS_OFFSET, centerx=tricky_centerx))

            self.matris.draw_surface()

        pygame.display.flip()

    def info_surf(self):

        textcolor = (255, 255, 255)
        font = pygame.font.Font(None, 30)
        width = (WIDTH-(MATRIS_OFFSET+BLOCKSIZE*MATRIX_WIDTH+BORDERWIDTH*2)) - MATRIS_OFFSET*2

        def renderpair(text, val):
            text = font.render(text, True, textcolor)
            val = font.render(str(val), True, textcolor)

            surf = Surface((width, text.get_rect().height + BORDERWIDTH*2), pygame.SRCALPHA, 32)

            surf.blit(text, text.get_rect(top=BORDERWIDTH+10, left=BORDERWIDTH+10))
            surf.blit(val, val.get_rect(top=BORDERWIDTH+10, right=width-(BORDERWIDTH+10)))
            return surf

        scoresurf = renderpair("Score", self.matris.score)
        levelsurf = renderpair("Level", self.matris.level)
        linessurf = renderpair("Lines", self.matris.lines)
        combosurf = renderpair("Combo", "x{}".format(self.matris.combo))

        height = 20 + (levelsurf.get_rect().height +
                       scoresurf.get_rect().height +
                       linessurf.get_rect().height +
                       combosurf.get_rect().height )

        area = Surface((width, height))
        area.fill(BORDERCOLOR)
        area.fill(BGCOLOR, Rect(BORDERWIDTH, BORDERWIDTH, width-BORDERWIDTH*2, height-BORDERWIDTH*2))

        area.blit(levelsurf, (0,0))
        area.blit(scoresurf, (0, levelsurf.get_rect().height))
        area.blit(linessurf, (0, levelsurf.get_rect().height + scoresurf.get_rect().height))
        area.blit(combosurf, (0, levelsurf.get_rect().height + scoresurf.get_rect().height + linessurf.get_rect().height))

        return area

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
