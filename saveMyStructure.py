#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from atomGenerator import *
from pointConverter import *


def main():
    fname = sys.argv[1]
    # atoms = polimerCircle(40)
    atoms = polimerLine(40)
    # atoms = randomAtoms(40, 10)
    savePointsAsPdb(atoms, "{}.pdb".format(fname))


if __name__ == '__main__':
    main()
