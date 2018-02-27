#!/usr/bin/python
from configparser import ConfigParser
 
 
def config_db(filename='database.ini', section='postgresql'):
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


def config_csv(filename='database.ini', section='file_csv'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    file_csv = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            file_csv[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return file_csv


def config_table(filename='database.ini', section='table_csv'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    table = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            table[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return table


