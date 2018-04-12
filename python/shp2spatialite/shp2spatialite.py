#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 2

import os
from sqlite3 import dbapi2 as db


db_folder = "/home/x12239181/qgis-tips-tricks/python/shp2spatialite/"
db_name = "test"
shp_folder = "/home/x12239181/qgis-tips-tricks/python/shp2spatialite/territorios"
table_name = "territorio"
encoding = "WINDOWS-1252"
srid = "4326"

"""Ceating Database"""
print "Creating Database..."
os.putenv("SPATIALITE_SECURITY", "relaxed")
conn = db.connect(db_folder + db_name + ".sqlite")
conn.enable_load_extension(True)
conn.execute("SELECT load_extension('mod_spatialite')")
# Init Spatial Metadata
conn.execute('SELECT InitSpatialMetadata(1)')
conn.commit()

"""Import a ESRI Shapefile to a SPATIALITE database
shp_folder = Full path to Esri Shapefile, don't use .shp on shapefile name
table_name = name to imported ESRI Shapefile
encoding = SPH atribute table encoding
srid =  System Coordinate ID in proj4"""

cur = conn.cursor()
sql = """SELECT ImportSHP("{shp_folder}", "{table_name}", '{encoding}', {srid});"""\
    .format(shp_folder=shp_folder, table_name=table_name, encoding=encoding, srid=srid)
cur.executescript(sql)
conn.commit()
conn.close()


