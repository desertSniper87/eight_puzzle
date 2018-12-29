#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 29.12.2018
# Last Modified Date: 29.12.2018

CONST_DIM = 6

def max():
    """TODO: Docstring for max.
    :returns: TODO

    """
    return CONST_DIM**2 - 1

def make_goal_matrix():
    goal = [0 for x in range(CONST_DIM) for y in range(CONST_DIM)]
    return goal


class Solver(object):
    """Docstring for Solver. """

    # Board initial

    def __init__(self):
        """TODO: to be defined1. """

class Board(object):

    """Docstring for Board. """


    def __init__(self):
        """TODO: to be defined1. """

        self.a = None
        self.f = 0
        self.g = 0
        self.h = self.manhattan()



    @classmethod
    def board_from_blocks(cls, blocks):
        cls.a = blocks


    def print_elements(self):
        """TODO: Docstring for print_elements.
        :returns: None

        """

        print(self.a)

    def is_goal(self):
        """TODO: Docstring for is_goal.
        :returns: bool

        """
        goal = make_goal_matrix()
        n = 1
        for i in range(CONST_DIM):
            for j in range(CONST_DIM):
                goal[i][j] = c

                if c == max():
                    c = 0

                else:
                    c+=1

                if self.a[i][j] != goal[i][j]:
                    return False


        return True


    def hamming(self, arg1):
        """TODO: Docstring for hamming.

        :arg1: TODO
        :returns: TODO

        """
        goal = make_goal_matrix()
        c = 0
        hamming = 0

        for i in range(CONST_DIM):
            for j in range(CONST_DIM):
                goal[i][j] = c

                if c == max():
                    c = 0

                else:
                    c+=1

                if self.a[i][j] != 0 and self.a[i][j] != goal[i][j]:
                    hamming += 1


        return hamming

    def manhattan(self):
        """TODO: Docstring for manhattan.
        :returns: TODO

        """
        
        goal = make_goal_matrix()



 










