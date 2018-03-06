# QGIS, tips & tricks - PYTHON - gedal_recursive

### Autor: Kyle Felipe
### Data: 06/03/2018

O script surgiu de uma necessidade de um colega no grupo do [Qgis Brasil](https://groups.google.com/forum/#!forum/qgisbrasil).
A intenção é, utilizar o comando [gedal_translate](http://www.gdal.org/gdal_translate.html) nos arquivos que estiverem dentro de pastas e subpastas, utilizando __Python__. 
A transformação só será feita nos formatos de arquivos que baterem com o informado.
O arquivo transformado é gerado na mesma pasta do arquivo original.

Como exemplo, o script procura por um aquivo .asc dentro das pastas e o trasnforma para o GTiff

Pode ser utilizado no _Python 2_ ou superior, e não é necessária a instalação de nenhum pacote adicional.

## Modo de uso

python gdal_recursive.py <EPSG> <"endereço_da_pasta">
<EPSG>: deve ser substituido pelo número do EPSG utilizado nos arquivos que deseja fazer a transformação
<"endereço_da_pasta"> o endereço absoluto da pasta que deseja rodar a transformação, sempre deve ser informada entre aspas duplas "".

* Exemplo: > python gdal_recursive.py 4674 "/home/temp"


## gdal_recursive.py

É o arquivo principal, contendo todo as funções do Python necessárias para rodar o comando gedal_translate.
contem duas variáveis globais e as funções utilizadas:

* _Variável_ format_in: É a extensão do formato a ser transformado.
* _Variável_ format_out: É a extensão do formato transformado que foi gerado.

* list_path(path): É a função que verifica as pastas que possuem arquivos com a extensão informada na variável format_in, ela precisa de um caminho (path) para analizar, e retorna uma lista com as pastas que possuem arquivos que batem com a extensão.
* find_file(path): É a função que procura dentro da pasta os arquivos que batem com a extensão.
* run_gdal(epsg, file_path, file): É a função que roda o comando gdal_translate para cada arquivo dentro da pasta.

Os códigos podem ser alterados conforme a necessidade de utilização.
