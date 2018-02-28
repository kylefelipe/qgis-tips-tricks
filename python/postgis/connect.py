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
    join_params = config.config(filename='database.ini', section='join_table')
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
        sql_count = """SELECT count(*) from {schema}.{table};""".format(schema=join_params["schema"],
                                                                        table=join_params["table"])
        cur.execute(sql_count)
        retorno = cur.fetchone()
        print(retorno)

        # Creating tabel acording to database.ini [table] and importing a csv file.

        print("Creating tabel {}...".format(table_params["table"]))
        sql_create = ("""CREATE TABLE IF NOT EXISTS {schema}.{table} (id bigserial, 
        {columns} text);""".format(schema=table_params["schema"], table=table_params["table"], columns=open_csv()[1]))
        cur.execute(sql_create)
        print(sql_create)

        # Importing data from CSV
        print("Importing CSV file...")
        sql_copy = (
            """COPY {schema}.{table} ({columns}) FROM STDIN 
            WITH (FORMAT CSV, HEADER, DELIMITER '{delim}');""".format(schema=table_params["schema"],
                                                                      table=table_params["table"],
                                                                      columns=str.join(" ,", open_csv()[0]),
                                                                      delim=csv_params["delimiter"]))
        csv_stdin = open(file=csv_params["path"], mode="r", newline='')

        cur.copy_expert(sql=sql_copy, file=csv_stdin)
        csv_stdin.close()
        print("Import done...\nJoing tables...")

        # Joining tables
        sql_join = """CREATE OR REPLACE VIEW {schema}.join_csv_teste AS
        SELECT a.id, a.municipio, a.coluna_1, a.coluna_2,b.{geometry}
        FROM {table_csv} as a, {join_table} as b
        WHERE a.{csv_key}::text = b.{join_key};""".format(schema=join_params["schema"],
                                                          geometry=join_params["geometry"],
                                                          table_csv=table_params["table"],
                                                          join_table=join_params["table"],
                                                          csv_key=table_params["key"],
                                                          join_key=join_params["key"]
                                                          )
        cur.execute(sql_join)

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
