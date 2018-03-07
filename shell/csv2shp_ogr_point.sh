#!/bin/bash
#GPL2 by yjmenezes at gmail.com versao 1.0 $2011-08-10
# http://www.gdal.org/ogr/drv_vrt.html
# CSV to SHP WGS84=EPSG:4326
# alguns testes com arquivos CSV e preparacao para o QuantumGIS
# dependencias: sudo apt-get update; apt-get install gdal-bin
echo $(basename $0) 1>&2
MY_DIR=/tmp
cd $MY_DIR
rm mylayer* sample*
# criando um arquivo de dados de exemplo com 4 campos, poderiam ser mais.
# linha 1 contem nome dos campos, e deve ser coerente com o arquivo *vrt
cat << eof | grep -v ^\# > sample1_g84.csv 
longgg,latggg,pname,z
-49.29,-25.39,p01,960.0
-49.29,-25.37,p02,961.0
-49.32,-25.37,p03,962.0
-49.32,-25.39,p04,963.0
eof
# converte de csv para dbf
# ogr2ogr -f "ESRI Shapefile" $MY_DIR sample1_g84.csv
# cria arquivo vrt (virtual format) descrevendo os dados de entrada
cat << eof > sample1_g84.vrt
<OGRVRTDataSource>
  <OGRVRTLayer name="mylayer1_g84">
    <SrcDataSource relativeToVRT="1">$MY_DIR</SrcDataSource>
    <SrcLayer>sample1_g84</SrcLayer>
    <GeometryType>wkbPoint</GeometryType>
    <LayerSRS>WGS84</LayerSRS>
    <GeometryField encoding="PointFromColumns" x="longgg" y="latggg"/>
  </OGRVRTLayer>
</OGRVRTDataSource>
eof
# transforma em shp
ogr2ogr -f "ESRI Shapefile" $MY_DIR sample1_g84.vrt
# lista as informacoes
ogrinfo -al mylayer1_g84.shp
# transtorma em UTM
ogr2ogr -t_srs "+proj=utm +zone=22 +south  +datum=WGS84" mylayer1_u84.shp mylayer1_g84.shp -nlt POINT
# listando as informacoes em UTM
ogrinfo -al mylayer1_u84.shp
# gerando o kml
ogr2ogr -f "KML" -t_srs EPSG:4326 mylayer1_g84.kml mylayer1_g84.shp 
exit 0      
# some ideas from: http://casoilresource.lawr.ucdavis.edu/drupal/book

