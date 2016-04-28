#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform
import sys
import argparse


def randomAtoms(n, d):
    """Generuje losowe położenie ułożenie atomów.
        n - liczba atomów
        d - rozmiar pudełka
    """
    atoms = []
    for i in xrange(n):
        x = uniform(0,d)
        y = uniform(0,d)
        z = uniform(0,d)
        atoms.append((x,y,z))
    return atoms

def polimerLine(n):
    """
        Atomy są ułożone na linii w osi X począwszy od punktu (0,0)
        n - liczba atomów
    """
    atoms = []
    for i in xrange(n):
        x = i
        y = 0
        z = 0 
        atoms.append((x,y,z))
    return atoms

def polimerCircle(n):
    """
        Atomy ułożone są na okręgu.
    """
    from math import cos
    from math import sin
    from math import pi
    from math import radians
    atoms = []
    angleIncrement = 360 / float(n)
    radius = 1/(2*sin(radians(angleIncrement)/2.)) # Odległość co 1
    for i in xrange(n):
        x = radius * cos(angleIncrement * i * pi/180)    
        y = radius * sin(angleIncrement * i * pi/180)    
        z = 0
        atoms.append((x,y,z))
    return atoms
    
if __name__ == '__main__':
    main()
