#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: yjmenezes cartognu.org  2017-06-27  QGIS
# sudo apt-get update; sudo apt-get install python-pip
# sudo pip intall --upgrade pip; sudo pip install sqlite3
import sys
import sqlite3.dbapi2 as db
def usage():
    print """
    Script tosco mostrando como gerar paralelas de 26m usando Spatialite.
    Precisa de um banco de dados trator.sqlite contendo a linha de referencia.
    """

if __name__ == '__main__':
    try:
        con = db.connect('paracatu.sqlite')
        # loading extension on connect:
        con.enable_load_extension(True)
        con.execute("SELECT load_extension('mod_spatialite');")
        cursor = con.execute('SELECT sqlite_version(), spatialite_version()')
        dados = list(cursor.fetchall())
        # Output should be something like:[(3.8.7.1, 4.1.1)]
        print "SQLITE VERSION:", dados[0][0]
        print "SPATIALITE VERSION: ", dados[0][1]

        # Creating table paracatu_paralelas to receive the new lines.
        con.executescript("""CREATE TABLE IF NOT EXISTS paracatu_paralelas (id INTEGER PRIMARY KEY AUTOINCREMENT);
        SELECT AddGeometryColumn ('paracatu_paralelas', 'geom', 32723, 'LINESTRING', 'XY');""")
        con.commit()

        # trator paralell lines, centimeter, for 130m range
        sql2 = """"""
        for distancia in range(145,13000,145):
            sql="""INSERT INTO paracatu_paralelas(geom)
			SELECT ST_OffsetCurve(geometry,%.2f) from paracatu;\n""" % (distancia / 100.0)
            sql2 += sql

        for distancia in range(145,13000,145):
            # print distancia
            sql="""INSERT INTO paracatu_paralelas(geom)
			SELECT ST_OffsetCurve(geometry,-%.2f) from paracatu;""" % (distancia / 100.0)
            sql2 += sql
        print sql2
        con.executescript(sql2)
        con.commit()
        con.close()
        print "Linhas paralelas geradas com sucesso...."


    except:
        usage()
    sys.exit(0)
