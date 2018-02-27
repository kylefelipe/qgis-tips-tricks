#!/usr/bin/python3
# -*- coding: utf-8 -*-
# http://www.postgresqltutorial.com/postgresql-python/connect/
# Author: Julio Menezes
# Mod by: Kyle Felipe
# sudo apt-cache search psycopg2
# sudo apt-get install python3-psycopg2

import psycopg2
import csv
import config

csv_params = config.config(filename='database.ini', section='file_csv')
table_params = config.config(filename='database.ini', section='table_csv')


def open_csv():
    """ Open the CSV file"""
    with open(file=csv_params["path"], encoding="utf8", mode="r", newline='') as csv_file:
        rows = list(csv.reader(csv_file, delimiter=csv_params["delimiter"]))
        heading = rows[0]
        sql = str.join(" text, ", heading)
        # print("ok")
        return heading, sql


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.config(filename='database.ini', section='postgresql')
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT PostGIS_Full_Version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        cur.execute('SELECT count(*) from public."Limites Municipais";')
        retorno = cur.fetchone()
        print(retorno)

        # Creating tabel acording to database.ini [table] and importing a csv file.

        print("Creating tabel {}...".format(table_params["table"]))
        sql_create = ("""CREATE TABLE {schema}.{table} (id bigserial, 
        {columns} text);""".format(schema=table_params["schema"], table=table_params["table"], columns=open_csv()[1]))
        cur.execute(sql_create)
        print(sql_create)

        # Importing data from CSV
        print("Importing CSV file...")
        csv_stdin = open(file=csv_params["path"], mode="r", newline='')

        cur.copy_from(csv_stdin.readlines()[1:], table=table_params["table"], sep=csv_params["delimiter"],columns=open_csv()[0])
        csv_stdin.close()

        # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()
