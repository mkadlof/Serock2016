#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pointConverter import *
from atomGenerator import *

def main():
    atoms = polimerCircle(40) 
    savePointsAsGro(atoms, "mojaStruktura.gro", "okręg 40 atomów")
    savePointsAsPdb(atoms, "mojaStruktura.pdb")

if __name__ == '__main__':
    main()
