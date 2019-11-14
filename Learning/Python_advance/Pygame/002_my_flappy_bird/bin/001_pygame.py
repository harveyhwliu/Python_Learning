#!/usr/bin/python2
#-*-coding:utf-8-*-
import pygame                   # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
from sys import exit            # 导入sys库中的exit函数

def demo1():
    """
    创建一个有背景图的窗口，并把小鸟移动画出来
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    size = SCREEN_WIDTH,SCREEN_HEIGHT

    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode(size)     # 初始化一个用于显示的窗口
    pygame.display.set_caption('my flappy brids games')       # 设置窗口标题

    #载入背景图
    background = pygame.image.load(r'../resources/flybird/bg_day.png')

    #小鸟
    color = (0, 0, 0)  # 设置颜色
    ball = pygame.image.load(r'../resources/flybird/bird0_0.png')  # 加载图片
    ballrect = ball.get_rect()  # 获取矩形区域
    speed = [5, 5]  # 设置移动的X轴、Y轴



    #事件循环(main loop)
    while True:
        #事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#退出
                pygame.quit()
                exit()

        #小鸟每次都移动移动
        ballrect = ballrect.move(speed)     # 移动小鸟
        screen.blit(background,(0,0))       # 绘制背景图
        screen.blit(ball, ballrect)         # 然后在绘制移动后的小鸟
        pygame.display.update()             # update 或者flip()  update 更优


    pygame.quit()#退出pygame


def demo2():
    """
    给小鸟加上碰撞检测
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    size = SCREEN_WIDTH,SCREEN_HEIGHT

    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode(size)     # 初始化一个用于显示的窗口
    pygame.display.set_caption('my flappy brids games')       # 设置窗口标题

    #载入背景图
    background = pygame.image.load(r'../resources/flybird/bg_day.png')

    #小鸟
    color = (0, 0, 0)  # 设置颜色
    ball = pygame.image.load(r'../resources/flybird/bird0_0.png')  # 加载图片
    ballrect = ball.get_rect()  # 获取矩形区域
    speed = [5, 5]  # 设置移动的X轴、Y轴



    #事件循环(main loop)
    while True:
        #事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#退出
                pygame.quit()
                exit()

        #移动小鸟
        ballrect = ballrect.move(speed)

        #给小鸟增加上 碰撞检测   如果碰到了四周则 运动方向朝反方向继续运动
        if( ballrect.left < 0 or ballrect.right >=SCREEN_WIDTH ):
            speed[0] = -speed[0]
        if (ballrect.top <0 or ballrect.bottom >=SCREEN_HEIGHT ):
            speed[1] = -speed[1]

        #获取小鸟的最新位置
        screen.blit(background,(0,0))       # 绘制背景图
        screen.blit(ball, ballrect)         # 然后在绘制移动后的小鸟
        pygame.display.update()             # update 或者flip()  update 更优

    pygame.quit()#退出pygame



def demo3():
    """
    给小鸟加上 移动速度的限制
    :return:
    """
    # 定义窗口的分辨率
    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    size = SCREEN_WIDTH,SCREEN_HEIGHT

    # 初始化游戏
    pygame.init()                   # 初始化pygame,返回结果是  成功初始化的模块的数量以及发生错误的模块的数量
    screen = pygame.display.set_mode(size)     # 初始化一个用于显示的窗口
    pygame.display.set_caption('my flappy brids games')       # 设置窗口标题

    #载入背景图
    background = pygame.image.load(r'../resources/flybird/bg_day.png')

    #小鸟
    color = (0, 0, 0)  # 设置颜色
    ball = pygame.image.load(r'../resources/flybird/bird0_0.png')  # 加载图片
    ballrect = ball.get_rect()  # 获取矩形区域
    speed = [5, 5]  # 设置移动的X轴、Y轴

    #设置 时钟
    clock = pygame.time.Clock()   #创建一个对象来帮助跟踪时间

    #事件循环(main loop)
    while True:
        #事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#退出
                pygame.quit()
                exit()

        #设置每次执行的时间
        clock.tick(10)     #tick(framerate=0) -> milliseconds,通过设置的framerate，限制游戏的运行速度

        #移动小鸟
        ballrect = ballrect.move(speed)

        #给小鸟增加上 碰撞检测   如果碰到了四周则 运动方向朝反方向继续运动
        if( ballrect.left < 0 or ballrect.right >=SCREEN_WIDTH ):
            speed[0] = -speed[0]
        if (ballrect.top <0 or ballrect.bottom >=SCREEN_HEIGHT ):
            speed[1] = -speed[1]

        #获取小鸟的最新位置
        screen.blit(background,(0,0))       # 绘制背景图
        screen.blit(ball, ballrect)         # 然后在绘制移动后的小鸟
        pygame.display.update()             # update 或者flip()  update 更优

    pygame.quit()#退出pygame




def main():
    # demo1()
    # demo2()
    demo3()



if __name__ == '__main__':
    main()
