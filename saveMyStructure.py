#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pointConverter import *
from atomGenerator import *
import sys

def main():
    fname = sys.argv[1]
    atoms = polimerCircle(40) 
    atoms = polimerLine(40) 
    atoms = randomAtoms(40, 10)
    savePointsAsGro(atoms, "{}.gro".format(fname), "okręg 40 atomów")
    savePointsAsPdb(atoms, "{}.pdb".format(fname))
    savePointsAsXYZ(atoms, "{}.xyz".format(fname))

if __name__ == '__main__':
    main()
