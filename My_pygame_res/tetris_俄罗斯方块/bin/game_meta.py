#-*- coding:utf-8 -*-
#通用的接口

import pygame
from random import choice

class ICommonMethod(object):
    """
    通用接口类
    """
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
