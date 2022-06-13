# QGIS tips & tricks - PYTHON - generate_label
_QGIS VERSION:_ 3.xx.xx

Esse script gera uma nova camada virtual com a nova coluna com o rótulo da feição, ordenada pela área da geometria

__NOTE:__ É necessário que haja uma camada ativa no painel de camadas para funcionar.

USAGE:

Abra esse script no console python do [Qgis](www.qgis.org) e com a camada ativa rode o script.

## Docs

Variáveis que podem ser editadas no script

* `virtual_layer_name` = Nome da camada virtual a ser gerada
* `new_column` = Nome do campo novo
* `prefix` = prefixo do campo novo - esta linha nao pode ser removida (Ex: A - 1, A - 2)
* `sufix` = Sufixo - esta linha nao pode ser removida (Ex: 1 - A, 2 - A)
* `dest_EPSG` = EPSG no qual deseja fazer o calculo de área (Ex: 31983)
