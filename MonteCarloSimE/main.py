# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:15:43 2021

@author: elifc
"""
from ec import TicToc, FindE
from threading import Thread
import os

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 100000000
    find_es = []
    threads = []
    for i in range(os.cpu_count()):
        find_es.append(FindE())
        threads.append(Thread(target=find_es[i].number_of_x, args=(n,)))
        print("Started thread number %d" % i)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    num = 0
    tot = 0
    for find_e in find_es:
        num += find_e.n
        tot += n
    e = num / tot

    print("e = %.8f | TIME = %.5f" % (e, tt.toc()))


    
