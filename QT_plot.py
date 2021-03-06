#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import Queue as qu

from QuadTree import QuadTree as QT

class Rect:
    def __init__(self, pt1, pt2):
        self.topright   = (max(pt1[0], pt2[0]), max(pt1[1], pt2[1]))
        self.bottomleft = (min(pt1[0], pt2[0]), min(pt1[1], pt2[1]))


def QTdivision(tree, area):
    queue = qu.Queue()
    queue.put((tree.root, area))
    
    while queue.empty() == False:
        (node, rect) = queue.get()
        for i in range(0, 4):
            if node.region[i] is None: pass
            else:
                if   i == 0: subarea = Rect(rect.topright, (node.x, node.y))
                elif i == 1: subarea = Rect((node.x, rect.topright[1]), (rect.bottomleft[0], node.y))
                elif i == 2: subarea = Rect(rect.bottomleft, (node.x, node.y))
                else:        subarea = Rect((rect.topright[0], node.y), (node.x, rect.bottomleft[1]))
                queue.put((node.region[i], subarea))
                
        x = [rect.bottomleft[0], rect.topright[0]]
        xline = [node.y, node.y]
        y = [rect.bottomleft[1], rect.topright[1]]
        yline = [node.x, node.x]
        
        plt.plot(x, xline, 'r-')    # division line
        plt.plot(yline, y, 'r-')    # division line
        plt.plot(node.x, node.y, 'bo')
        
    plt.show()
            
        
if __name__ == "__main__":
    
    from QuadTree import QuadTree as QT

    nodeNum = 300
    
    # Generate random numbers from discrete uniform distribution.
    # x = np.random.random_integers(-100, 100, nodeNum)
    # y = np.random.random_integers(-100, 100, nodeNum)

    # Generate random numbers from discrete standard normal distribution.
    x = np.random.randint(-100, 100, nodeNum)
    y = np.random.randint(-100, 100, nodeNum)

    # Generate random numbers from normal distribution
    # x = np.random.normal(0, 20, nodeNum)
    # y = np.random.normal(0, 20, nodeNum)
    
    lst = [(x[i], y[i]) for i in range(nodeNum)]

    qt = QT()
    qt.makeOptQT(lst)    
    area = Rect((max(x), max(y)), (min(x), min(y)))
    QTdivision(qt,area)    
