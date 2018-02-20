#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# author: yjmenezes cartognu.org  2017-06-27  QGIS
# sudo apt-get update; sudo apt-get install python-pip
# sudo pip intall --upgrade pip; sudo pip install sqlite3
import sys
import sqlite3.dbapi2 as db
from os import putenv


def usage():
    print """
    Script tosco mostrando como gerar paralelas de 1.45m usando Spatialite.
    Precisa de um banco de dados trator.sqlite contendo a linha de referencia.
    """


if __name__ == '__main__':
    try:
        putenv("SPATIALITE_SECURITY", "relaxed")
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
        con.executescript("""CREATE TABLE IF NOT EXISTS linhas_paralelas (id INTEGER PRIMARY KEY AUTOINCREMENT);
        SELECT AddGeometryColumn ('linhas_paralelas', 'geom', 32723, 'LINESTRING', 'XY');""")
        con.commit()

        # trator paralell lines, centimeter, for 130m range
        distancia = []
        # Linhas do lado esquerdo (negativo)
        for i in range(145, 13000, 145):
            distancia.append((float(i)/100)*-1)
        # linhas do lado direito (positivo)
        for i in range(145, 13000, 145):
            distancia.append((float(i)/100))
        # print distancia
        sql = """INSERT INTO linhas_paralelas(geom)
        SELECT ST_OffsetCurve(geometry, ?) from paracatu;"""
        sql2 = ""
        for i in distancia:
            sql2 += """INSERT INTO linhas_paralelas(geom)
        SELECT ST_OffsetCurve(geometry,{dist}) from paracatu;\n""".format(dist=i)
        con.executescript(sql2)
        con.commit()
        con.close()
        print "Foram geradas {qt} linhas paralelas com sucesso....".format(qt=len(distancia))


    except:
        usage()
    sys.exit(0)
