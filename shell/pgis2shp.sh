#!/bin/bash
# GPL2 yjmenezes at gmail.com ver 1.0 2018-03-25
# export PostGIS tables to shapefile
# tablenames must have 10 characters, max due SHP limitations;
# to be used at server side host=localhost
if [ $# -lt 3 ]; then
    echo $(basename $0) "dbname username userpass"
    exit 1
fi
DB=$1
OWN=$2
PAS=$3
OUT=/tmp/pgout
mkdir -p $OUT
rm $OUT/*
cd $OUT
psql $1 -U $2 -w -c "SELECT table_name FROM information_schema.tables 
 WHERE table_schema='public' AND table_type='BASE TABLE';" | \
awk 'NR > 2 { print $0 }' | grep -v -e \( -e ^$ -e spatial  | \
while read tabname; do
    echo "processing" $tabname 1>&2
    pgsql2shp -u $OWN -P $PAS -f $OUT/$tabname $DB $tabname
done
echo "please check" $OUT
ls $OUT/*shp 1>&2
exit 0
#----------------------------------------------------------------------------
