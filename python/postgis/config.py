#!/usr/bin/python3
# -*- coding: utf-8 -*-
from configparser import ConfigParser
 
 
def config(filename='', section=''):
    """ This parser takes settings from a file .ini"""
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db
