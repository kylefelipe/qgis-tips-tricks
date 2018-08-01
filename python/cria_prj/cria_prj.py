#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Julio Menezes cartognu.org#
# ver 1.0  python 2.7.x , 2018-08-01, GNU/Linux Debian stretch 9.5
import sys
from osgeo import ogr, osr
#
def uso():
    sys.stderr.write ('Digite apenas numeros do EPSG\n')
    sys.stderr.write ('''
    exemplo de uso:
       python3  cria_prj.py  31985
       python   cria_prj.py  31985
       posteriormente copie o proj4.prj com o nome do seu conjundo shapefile.
    ''')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        uso()
    spatialRef = osr.SpatialReference()
    spatialRef.ImportFromEPSG(int(sys.argv[1]))
    spatialRef.MorphToESRI()
    file = open('proj4.prj', 'w')
    file.write(spatialRef.ExportToWkt())
    file.close()
    sys.exit(0)
