#!/usr/bin/python
#http://www.postgresqltutorial.com/postgresql-python/connect/
# sudo apt-cache search psycopg2
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
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
        
        cur.execute('SELECT count(*) from cadastros;')
        retorno = cur.fetchone()
        print(retorno)

       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()
