#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform


def randomAtoms(n, d):
    """Generuje losowe położenie ułożenie atomów.
        n - liczba atomów
        d - rozmiar pudełka
    """
    atoms = []
    for _ in xrange(n):
        x = uniform(0, d)
        y = uniform(0, d)
        z = uniform(0, d)
        atoms.append((x, y, z))
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
        atoms.append((x, y, z))
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
    angle_increment = 360 / float(n)
    radius = 1 / (2 * sin(radians(angle_increment) / 2.))  # Odległość co 1
    for i in xrange(n):
        x = radius * cos(angle_increment * i * pi / 180)
        y = radius * sin(angle_increment * i * pi / 180)
        z = 0
        atoms.append((x, y, z))
    return atoms


if __name__ == '__main__':
    main()
