#!/usr/local/bin/python
#-*- coding:utf-8 -*-

from collections import namedtuple

class TetrisMeta(object):
    """
    俄罗斯方块  游戏基础类
    """

    def __init__(self):
        self.__tetris_meta_info = namedtuple("__tetris_meta_inf0", "name color shape")#名称 颜色 形状
        self.construct_based_tetris_shape()


    def construct_based_tetris_shape(self):
        """
        构造基础的 俄罗斯方块游戏中的 图形
        :return:
        """

        l = self.__tetris_meta_info(name="l",
                           color="blue",
                           shape=((0,0,0,0),
                                  (1,1,1,1),
                                  (0,0,0,0),
                                  (0,0,0,0)))
        l_1 = self.__tetris_meta_info(name="l1",
                           color="blue",
                           shape=((0,1,0,0),
                                  (0,1,0,0),
                                  (0,1,0,0),
                                  (0,1,0,0)))
        square = self.__tetris_meta_info(name="square",
                             color="yellow",
                             shape=((1,1),
                                    (1,1)))
        
        t_up = self.__tetris_meta_info(name="t_up",
                          color="pink",
                          shape=((0,1,0),
                                 (1,1,1),
                                 (0,0,0)))

        t_down = self.__tetris_meta_info(name="t_down",
                          color="pink",
                          shape=((0,0,0),
                                 (1,1,1),
                                 (0,1,0)))

        snake_r = self.__tetris_meta_info(name="snake_r",
                                  color="green",
                                  shape=((0,1,1),
                                         (1,1,0),
                                         (0,0,0)))
        
        snake_l = self.__tetris_meta_info(name="snake_l",
                                 color="red",
                                 shape=((1,1,0),
                                        (0,1,1),
                                        (0,0,0)))
        
        gun_l = self.__tetris_meta_info(name="gun_l",
                               color="cyan",
                               shape=((1,0,0),
                                      (1,1,1),
                                      (0,0,0)))
        
        gun_r = self.__tetris_meta_info(name="gun_r",
                                color="orange",
                                shape=((0,0,1),
                                       (1,1,1),
                                       (0,0,0)))

        self.__based_tetris_shape_l = [l,l_1,square,t_up,t_down,snake_r,snake_l,gun_l,gun_r]

    def get_based_tetris_shape(self):
        """
        获取 基础的俄罗斯方块形状
        :return:
        """
        return self.__based_tetris_shape_l

    def rotate(self,shape, times=1):
        """
        图形的旋转  ， 右旋
        :param shape:  待旋转的图形
        :param times:  向右旋转的次数
        :return:
        """
        if times == 0:
            return shape
        times %= 4

        shape_row= len(shape)

        rotated = [[] for _ in range(shape_row)]

        # Rotate one time to the right
        for line in shape:
            for index, atom in enumerate(line):
                rotated[index].insert(0, atom)
        return tuple(map(tuple, rotated)) if times <= 1 else self.rotate(rotated, times-1)

    def rotate_left(self,shape, times=1):
        """
        图形的旋转，  左旋
        :param shape:
        :param times:
        :return:
        """
        return self.rotate(shape, 3) if times <= 1 else self.rotate_left(self.rotate(shape, 3), times-1)



def test():
    test_obj = TetrisMeta()
    tetromino_shapes = [t.shape for t in test_obj.get_based_tetris_shape()]
    #右旋
    for shape in tetromino_shapes:
        print "before:",shape
        new_shape = test_obj.rotate(shape,1)
        print "after:",new_shape

    #左旋
    for shape in tetromino_shapes:
        print "before:",shape
        new_shape = test_obj.rotate_left(shape,1)
        print "after:",new_shape


if __name__ == '__main__':
    test()
