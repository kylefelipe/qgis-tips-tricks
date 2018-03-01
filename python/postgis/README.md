# QGIS, tips & tricks - PYTHON - Postgis

O script surgiu de uma necessidade de um colega no grupo do [Telegram](https://telegram.org) ThinkFree - Qgis.
A intenção é inserir os dados de um aruivo CSV em um bando de dados [POSTGIS e fazer a união com uma](https://postgis.net/) e,
em seguida, fazer a união desses dados a uma tabela que já contenha geometria definida, georreferenciando os dados do CSV.

A tabela utilizada para fazer o georreferenciamento dos dados do CSV foi o do Limite Municipal de MG (IBGE).

__ATENÇÃO:__ É necessário a instalação do psycopg no Python antes de utilizar.

* [config.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/config.py): Código de busca a configuração dos dados para o [connect.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/connect.py)..
* [connect.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/connect.py): Script de inserção do CSV e cruzamento das tabelas.
* [database.ini](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/database.ini): Arquivo contendo os paramentos de conexo com o bd Postgis, do CSV e da tabela que será usada no georreferenciamento dos dados.
* [arquivo.csv](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/arquivo.csv): Aquivo utilizado no exemplo.
