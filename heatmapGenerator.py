#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import numpy
import matplotlib.pyplot as plt
from math import sqrt

def d(p1, p2):
    """point - three element tuple"""
    return sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 )

def fileToListOfPoints(filename):
    s = [i.strip().split() for i in open(filename)]
    points = []
    for i in s:
        points.append((float(i[0]), float(i[1]), float(i[2])))
    return points

def structureToMatrix(points):
    n = len(points)
    matrix = numpy.zeros((n,n))
    for i in xrange(n):
        for j in xrange(n):
            matrix[i,j] = d(points[i], points[j])
    return matrix

def createHeatmap(matrix, out_path = ''):
    """
        creates heatmap based on 2D matrix
        By default it shown in window, but may be saved to file if out_path provided.
    """
   
    plt.clf()
    plt.imshow(matrix, interpolation='none', cmap='Blues_r')

    if len(out_path) == 0:
        plt.show()    
    else:
        plt.savefig(out_path)
    
if __name__ == '__main__':
    main()
