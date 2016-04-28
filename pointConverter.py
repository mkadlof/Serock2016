#!/usr/bin/env python
# -*- coding: utf-8 -*-

points = [(1.1, 2.3, 3.4),
          (0.1, 5.3, 4.2),
          (9.2, 4.3, 1.3)]

def savePointsAsPdb(points, filename):
    """Przyjmuje liste krotek trzy elementowych i zapisuje je do pliku PDB o nazwie filename"""
    atoms = ''
    n = len(points)
    for i in xrange(n):
        x = points[i][0]
        y = points[i][1]
        z = points[i][2]
        atoms += ('{0:6}{1:>5}  {2:3}{3:}{4:3} {5:}{6:>4}{7:}   {8:8.3f}{9:8.3f}{10:8.3f}{11:6.2f}{12:6.2f}{13:>12}\n'.format("ATOM",i+1,'B',' ','BEA','A', i+1, ' ', x, y, z, 0, 0, 'C'))
    connects = 'CONECT    1    2\n'
    for i in xrange(2,n):
        connects += 'CONECT{:>5}{:>5}{:>5}\n'.format(i, i-1, i+1)
    connects += 'CONECT{:>5}{:>5}\n'.format(n,n-1)
    pdbFileContent = atoms + connects
    open(filename, 'w').write(pdbFileContent)

def savePointsAsGro(points, filename, comment="komentarz"):
    n = len(points)
    x,y,z = zip(*points)
    d = max(x+y+z)
    l = ["{}\n".format(comment)]
    l.append(str(n)+'\n')
    for i in xrange(n):
        x = points[i][0]
        y = points[i][1]
        z = points[i][2]
        w = '{:5}{:5}{:5}{:5}{:8.3f}{:8.3f}{:8.3f}\n'.format(i,"BEA","B",i+1,x,y,z)
        l.append(w)
    l.append('{0:5f} {0:5f} {0:5f}'.format(d))
    filename = '{}'.format(filename)
    open(filename, 'w').writelines(l)
    return filename

def main():
    savePointsAsPdb(points, 'mojaStruktura.pdb')
    savePointsAsGro(points, 'mojaStruktura.gro')

if __name__ == '__main__':
    main()
