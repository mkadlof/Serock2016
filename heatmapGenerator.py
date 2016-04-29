#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import numpy
import matplotlib.pyplot as plt


def createHeatmap(matrix, out_path = ''):
    """
        Tworzy obrazek z heatmapa na podstawie macierzy 2D.
        Domyslnie wyswietla ja w okienku, jezeli podano sciezke - zapisuje do pliku
    """
   
    plt.clf()
    plt.imshow(matrix, interpolation='none', cmap='Blues')

    #pcm = ax[1].pcolor(X, Y, Z1, cmap='PuBu_r')
    #plt.colorbar(pcm, ax=ax[1], extend='max')

    if len(out_path) == 0:
        plt.show()    
    else:
        plt.savefig(out_path)
    



if __name__ == '__main__':
    main()
