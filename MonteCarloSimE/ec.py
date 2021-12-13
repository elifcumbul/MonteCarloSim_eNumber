# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:24:09 2021

@author: elifc
"""
import random
import time
from numba import jit


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:
    def __init__(self):
        self.n = 0
        self.s = 0

    def number_of_x(self, nn):
        (self.n, self.s) = self.number_of_x_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def number_of_x_static(nn):
        n = 0
        s = 0
        for i in range(nn):
            count = 0
            while s < 1:
                count += 1
                x = random.random()
                s += x

            s = 0
            n += count
        return n, s

    def value_of_e(self, nn):
        return self.n / nn


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    time.sleep(5)
    print(tt.toc())
