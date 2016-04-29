#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heatmapGenerator import *
import sys

def main():
    s = fileToListOfPoints(sys.argv[1])
    matrix = structureToMatrix(s)
    createHeatmap(matrix)

if __name__ == '__main__':
    main()
