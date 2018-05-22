# -*- coding: utf-8 -*-
# Author: Kyle Felipe Vieira Roberto
# E-mail: kylefelipe@gmail.com
# Date: 2018/05/22

import os, sys
from os import sep as separador
from subprocess import call

format_in = ".shp"

def list_path(path):
    """ Get all sub-paths from a path if have a shapefile inside"""
    path_lits = []
    for path, directory, files in os.walk(path):
        for file_in in files:
            if file_in.lower().endswith(format_in):
                path_lits.append(path+separador+file_in)
    if len(path_lits) > 0:
        return set(path_lits)
    else:
        return False


def save_kml(file_in):
    """ Change savinf file shp to kml """
    file_out = file_in[:-4]+".kml"
    pasta =   str.join(separador, file_in.split(separador)[:-1])
    print "salvando arquivo {arquivo} na pasta {pasta}".format(arquivo=file_in.split(separador)[-1], pasta=pasta)
    command = "ogr2ogr", "-f","KML", """{arquivosaida}""".format(arquivosaida=file_out), """{file_in}""".format(file_in=file_in)
    call(command)


try:

    if len(sys.argv) > 1:
        print "Caminho:", sys.argv[1]
        if os.path.isdir(sys.argv[1]):
            if list_path(sys.argv[1]) is not False:
                for path in list_path(sys.argv[1]):
                    save_kml(path)
            else:
                print("No files with the extension '{}' was found!!!".format(format_in))
        else:
            print("Argument is not a valid path!")

except:
    print("Inform a valid path to use!!!")