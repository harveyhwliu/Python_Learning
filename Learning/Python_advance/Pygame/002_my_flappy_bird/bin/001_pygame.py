#!/usr/bin/python2
#-*-coding:utf-8-*-
import pygame                   # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
#pygame.locals模块里面包含了很多pygame需要用到的常量，例如set_mode里面窗口的标志（flags）、消息事件（event）的类型等等。
# 另外，程序想使用pygame.locals模块里面pygame的常量的话，只能使用“from pygame.locals import *”。
from sys import exit            # 导入sys库中的exit函数
import os


def demo1():
    """
    创建一个黑屏的窗口，并可以退出
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 640

    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # 初始化一个用于显示的窗口
    pygame.display.set_caption('This is my first pygame-program')       # 设置窗口标题

    #事件循环(main loop)
    while True:
        # 处理游戏退出
        # 从消息队列中循环取
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    pygame.quit()#退出pygame


def demo2():
    """
    创建一个有背景图的窗口
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 480
    size = SCREEN_WIDTH,SCREEN_HEIGHT
    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode(size)     # 初始化一个用于显示的窗口
    pygame.display.set_caption('This is my first pygame-program')       # 设置窗口标题

    #载入背景图
    background = pygame.image.load(r'../resources/s.png')


    #事件循环(main loop)
    while True:

        #绘制背景图
        screen.blit(background,(0,0))


        #更新屏幕  在这里多说一点，关于pygame.display.flip()和pygame.display.update()，文档上说，update更像是flip的优化版本，主要区别是flip是屏幕的整体刷新（entire），而update是局部刷新（portion）。
        pygame.display.update()

        # 处理游戏退出
        # 从消息队列中循环取
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    pygame.quit()#退出pygame



def demo3():
    """
    创建一个有背景图的窗口
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 480
    size = SCREEN_WIDTH,SCREEN_HEIGHT
    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode(size)     # 初始化一个用于显示的窗口
    pygame.display.set_caption('This is my first pygame-program')       # 设置窗口标题

    #载入背景图
    background = pygame.image.load(r'../resources/s.png')

    #小球
    ball= pygame.image.load(r'../resources/3.png')
    color = (0,0,0)
    ballrect = ball.get_rect()
    speed = [5,5] #设置移动的x轴，一周

    #事件循环(main loop)
    while True:

        #绘制背景图
        screen.blit(background,(0,0))

        #
        ballrect = ballrect.move(speed)
        screen.fill(color)
        screen.blit(ball,(10,10))

        pygame.display.flip()  # 更新全部显示

        #更新屏幕  在这里多说一点，关于pygame.display.flip()和pygame.display.update()，文档上说，update更像是flip的优化版本，主要区别是flip是屏幕的整体刷新（entire），而update是局部刷新（portion）。
        # pygame.display.update()

        # 处理游戏退出
        # 从消息队列中循环取
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    pygame.quit()#退出pygame


def main():
    # demo1()
    # demo2()
    demo3()

if __name__ == '__main__':
    main()
