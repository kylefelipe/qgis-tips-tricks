# QGIS, tips & tricks - PYTHON - Postgis

O script surgiu de uma necessidade de um colega no grupo do [Telegram](https://telegram.org) ThinkFree - Qgis.
A intenção é, utilizando __Python 3__, inserir os dados de um aruivo CSV em um banco de dados [POSTGIS](https://postgis.net/) e,
em seguida, fazer a união desses dados a uma tabela que já contenha geometria definida, georreferenciando os dados do CSV.

A tabela utilizada para fazer o georreferenciamento dos dados do CSV foi o do Limite Municipal de MG (IBGE).

__ATENÇÃO:__ É necessário a instalação do [psycopg](http://initd.org/psycopg/docs/index.html) no Python antes de utilizar.

É composto por:

* [config.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/config.py): Código de busca a configuração dos dados para o [connect.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/connect.py)..
* [connect.py](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/connect.py): Script de inserção do CSV e cruzamento das tabelas.
* [database.ini](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/database.ini): Arquivo contendo os paramentos de conexão com o bd Postgis, do CSV e da tabela que será usada no georreferenciamento dos dados.
* [arquivo.csv](https://github.com/kylefelipe/qgis-tips-tricks/blob/master/python/postgis/arquivo.csv): Aquivo utilizado no exemplo.


## database.ini

É um arquivo de configuração utilizado para auxiliar na conexão com o banco, acesso ao csv, a tabela com geometria, criação da tabela que irá receber o CSV e
a criação da tabela virtual com cruzamento das tabelas.
Esses parêmetros podem, e devem ser modificados conforme a necessidade de utilização.

Possui 3 sessões (sections) listadas a baixo:É o campo da tabela que será uitilizado como chave para fazer a união das tabelas.

* [postgresql]: Esssa sessão possui as informações de conexo com o banco.
  host: Endereço do banco de dados.
  port: Porta de acesso ao bd.
  database: nome do banco a ser acessado.
  user: nome do usuário a ser usado no acesso ao bd.
  password: senha de acsso ao banco.
  
 * [file_csv]: Essa sessão contem os dados referente ao arquivo CSV a ser importado para o banco.
  path: o caminho absoluto do arquivo.
  delimiter:caractere utilizado como delimitador dos dados dentro do arquivo CSV. Exemplo ; ou ,.
  key (remover essa tag)
  
 * [table_csv]: Contem os parâmetros da tabela que será criada para receber o arquivo CSV.
  schema: Nome do Schema onde a tabela será criada.
  table: Nome da tabela a ser criada que irá receber os dados do CSV.
  key: É o campo da tabela que será uitilizado como chave para fazer a união das tabelas.

* [join_table]: Contem os parâmetros da tabela do banco que ser utilizada na união para georreferenciar os dados do CSV.
  schema: Nome do Schema onde a tabela se encontra.
  table: Nome da tabela que será utilizada.
  key: É o campo da tabela que será uitilizado como chave para fazer a união das tabelas.
  geometry: É o nome do campo da tabela que contém a geometria.
  
## config.py

Esse aquivo possui a função "config()" que lê o arquivo database.ini e retorna um dicionario de dados das sessões contidas lá dentro, conforme o 
código principal vai precisando do dado.
Caso seja solicitado alguma sessão que não está contida nele, ele dispara um erro dizendo que a sessão não foi encontrada.

A função possui dois parâmetros a serem informados no momento da uilitzação:

* filename: Aqui é informado o nome do aquivo que possui a ser utilizado.
* section: Nome da sessão que deseja acessar.


## connect.py

É o arquivo principal, contendo todo os comandos python e SQL utilizados na inserção e cruzamento dos dados.
contem duas variáveis globais e as funções utilizadas:

* _Variáveis_: armazenam os dados que o arquivo config.py retorna de acordo com a sessão solicitada.

* open_csv(): Essa função foi feita para ler o CSV e buscar os cabeçalhos na primeira linha e retorna as colunas e um texto
básico com o cabeçalho da tabela a ser criada.

* connect(): Essa é a função principal, responsável por conectar ao banco de dados e fazer a manipulação do banco, como a criação 
da tabela que irá receber os dados do aquivo CSV, insere os dados e faz a união das tabelas.
Cada passo do processo possui um comentãrio relativo, e caso haja alugm erro de execussão nessa função, a criação da e cruzamento das 
tabelas não será executada.

Os códigos podem ser alterados conforme a necessidade de utilização.
