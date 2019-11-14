import pygame
from pygame.locals import *


class Pipeline(object):
    """定义一个管道类"""

    def __init__(self,score):
        """定义初始化方法"""
        self.wallx = 400  # 管道所在X轴坐标
        self.score = score    #  得分
        self.pineUp = pygame.image.load(r"../resources/pipe_down.png")
        self.pineDown = pygame.image.load(r"../resources/pipe_down.png")

    def updatePipeline(self):
        """"管道移动方法"""
        self.wallx -= 5  # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞越管道，分数加1，并且重置管道
        if self.wallx < -80:
            self.score += 1
            self.wallx = 400

    def get_score(self):
        """获取得分"""
        return self.score
