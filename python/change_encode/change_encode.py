# -*- coding: utf-8 -*-
# Author: Kyle Felipe Vieira Roberto
# E-mail: kylefelipe@gmail.com
# Date: 2018/03/13

import os, sys
from osgeo import ogr
from subprocess import call

format_in = ".shp"


def list_path(path):
    """ Get all sub-paths from a path if they have a shapefile inside"""
    path_lits = []
    # print("list_path:", path)
    for path, directory, files in os.walk(path):
        for file_in in files:
            if file_in.lower().endswith(format_in):
                path_lits.append(path)
    # print(set(path_lits))
    if len(path_lits) > 0:
        return set(path_lits)
    else:
        return False


def find_file(path):
    path_vector = []
    for i in os.listdir(path):
        if i.lower().endswith(format_in):
            path_vector.append(i)
    return path_vector


def run_ogr2ogr(file_in, encode):
    """ Change shapefile encoding using ogr2ogr """
    driver = ogr.GetDriverByName('ESRI Shapefile')

    # folder = str.join("/", (file_in.split("/")[:-1]))
    file_out = file_in[:-4]+"_ENCODE"+file_in[-4:]
    file_out2 = file_out

    command = "ogr2ogr", "-lco", "ENCODING={to_encode}".format(to_encode=encode), "{file_out}".format(file_out=file_out2),\
        "{file_in}".format(file_in=file_in)
    call(command)
    return "{}".format(file_out2)


try:

    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[2]):
            to_encode = sys.argv[1]
            if list_path(sys.argv[2]) is not False:
                for path in list_path(sys.argv[2]):
                    # print(">>:", path)
                    for file_in in find_file(path):
                        file_in2 = path + "/" + file_in
                        run_ogr2ogr(file_in=file_in2, encode=to_encode)
                print("Process finished...")
            else:
                print("No files with the extension '{}' was found!!!".format(format_in))

        else:
            print("Argument is not a valid path!")

except:
    print("Inform a valid path to use!!!")
