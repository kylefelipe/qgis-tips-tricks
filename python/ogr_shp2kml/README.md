# QGIS, tips & tricks - PYTHON - ogr_shp2kml

### Autor: Kyle Felipe
### Data: 22/05/2018

O script surgiu de uma necessidade de um colega do grupo [#ThinkFreeQgis](https://t.me/thinkfreeqgis) de salvar em KML arquivos shapefile dentro de um de [ogr2ogr](http://www.gdal.org/ogr2ogr.html) nos arquivos que estiverem dentro de pastas e subpastas, utilizando __Python__. 

Como exemplo, o script procura por um aquivo .shp dentro das pastas e o muda encoding para UTF-8

Pode ser utilizado no _Python 2_ , e é necessária a instalação do pacote osgeo.

## Modo de uso

python2 ogr_shp2kml.py <"endereço_da_pasta">
<"endereço_da_pasta"> o endereço absoluto da pasta que deseja rodar a transformação, sempre deve ser informada entre aspas duplas "" sem a barra no final.

* Exemplo: > python change_encode.py "UTF-8" "/home/temp"

Os códigos podem ser alterados conforme a necessidade de utilização.
