# -*- coding: utf-8 -*-
# Author: Kyle Felipe Vieira Roberto
# E-mail: kylefelipe@gmail.com
# Date: 2018/03/06

import os, sys
from subprocess import call


format_in = ".tif"
format_out = ".tif"


def list_path(path):
    """ Get all sub-paths from a path if have a tiff inside"""
    path_lits = []
    # print("list_path:", path)
    for path, directory, files in os.walk(path):
        for file in files:
            if file.lower().endswith(format_in):
                path_lits.append(path)
    # print(set(path_lits))
    if len(path_lits) > 0:
        return set(path_lits)
    else:
        return False


def find_file(path):
    path_tiff = []
    for i in os.listdir(path):
        if i.lower().endswith(format_in):
            path_tiff.append(i)
    return path_tiff


def run_gdal(epsg, file_path, file):
    """Run gedal process"""
    file_in = file_path+"/"+file
    # print("Entrada:", file_in)
    # print(str.split(file, "."))
    file_out = file_path+"/"+(str.split(file, ".")[0])+"_translate.tif"
    # print("Saida:", file_out)
    command = "gdal_translate", "-a_srs", "EPSG:{}".format(epsg), "-of", "GTiff", file_in, file_out
    print(command)
    call(command)


try:
    # print(len(sys.argv))
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[2]):
            epsg = sys.argv[1]
            # print(">: ", list_path(sys.argv[2]))
            print(sys.argv[2])
            if list_path(sys.argv[2]) is not False:
                for path in list_path(sys.argv[2]):
                    # print(">>:", path)
                    for file in find_file(path):
                        run_gdal(epsg, path, file)
            else:
                print("No files with the extension '{}' was found!!!".format(format_in))
        else:
            print("Argument is not a valid path!")

except:
    print("Inform a valid path to use!!!")
