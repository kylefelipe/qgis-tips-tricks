#!/bin/bash
# GPL2 yjmenezes at gmail.com ver 1.0 2018-03-25
# export PostGIS tables to OGC standard Geopackage using ogr2org
#TODO fix Incorrectly quoted string literal message.
if [ $# -lt 4 ]; then
    echo $(basename $0) "dbname  username  userpass  out.gpkg"
    exit 1
fi
DB=$1
OWN=$2
PAS=$3
PKG=$(basename $4 .gpkg)
OUT=/tmp/pgout
mkdir -p $OUT
rm $OUT/*
cd $OUT
psql $DB -U $OWN -w -c "SELECT table_name FROM information_schema.tables 
 WHERE table_schema='public' AND table_type='BASE TABLE';" | \
awk 'NR > 2 { print $0 }' | grep -v -e \( -e ^$ -e spatial  | \
while read tbname; do
    echo "packing" $tbname 1>&2
    ogr2ogr -f "GPKG" $OUT/$PKG".gpkg" -update -append  PG:"host=localhost user=$OWN dbname=$DB password=$PAS" $tbname
done
echo "please check" $OUT
ls $OUT/* 1>&2
exit 0
