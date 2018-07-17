# QGIS, tips & tricks - PYTHON - change_encode

### Autor: Kyle Felipe
### Data: 17/07/2018

O script surgiu de uma necessidade de mudar o SRC de diversos arquivos shapefiles, dentro de pastas e suas sub pastas para um determinado SRC.
A intenção é, utilizar o comando [ogr2ogr](http://www.gdal.org/ogr2ogr.html) nos arquivos que estiverem dentro de pastas e subpastas, utilizando __Python__.
A transformação só será feita nos formatos VETORIAIS de arquivos que baterem com o informado.
O arquivo transformado é gerado na mesma pasta do arquivo original.

Como exemplo, o script procura por um aquivo .shp dentro das pastas e o muda src para EPSG:4674

Pode ser utilizado no _Python 2_ ou superior, e é necessária a instalação do pacote osgeo.

## Modo de uso

python reproj_recursive.py <SRC> <"endereço_da_pasta">
<SRC>: deve ser substituido pelo SRC desejado sempre informado ente aspas duplas "".
<"endereço_da_pasta"> o endereço absoluto da pasta que deseja rodar a transformação, sempre deve ser informada entre aspas duplas "".

* Exemplo: > python reproj_recursive.py "EPSG:4677" "/home/temp"


## reproj_recursive.py

É o arquivo principal, contendo todo as funções do Python necessárias para rodar o comando ogr2ogr.
contem uma variável globai e as funções utilizadas:

* _Variável_ format_in: É a extensão do formato a a ter o src mudado.
* _Variável_ insrs: É a variável que armazena o SRS novo.

* list_path(path): É a função que verifica as pastas que possuem arquivos com a extensão informada na variável format_in, ela precisa de um caminho (path) para analizar, e retorna uma lista com as pastas que possuem arquivos que batem com a extensão.
* find_file(path): É a função que procura dentro da pasta os arquivos que batem com a extensão.
* run_ogr2ogr(file_in, srs): É a função que roda o comando ogr2ogr para cada arquivo dentro da pasta.

Os códigos podem ser alterados conforme a necessidade de utilização.
