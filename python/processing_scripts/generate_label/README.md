# QGIS tips & tricks - PYTHON - generate_label
_QGIS VERSION:_ 3.xx.xx  
_Processing toolbox_

Esse script gera uma nova camada virtual com a nova coluna com o rótulo da feição, ordenada pela área da geometria, sendo possível colocar um prefixo e um sufixo.

O novo campo receberá uma string (texto) no seguinte formato:

`<PREFIXO><POSICAO DA FEIÇÃO><SUFIXO>`
sendo a ordem 

USAGE:

Na caixa de ferramentas do processing clique no icone do [Python](www.python.org) e crie um novo script, cole o conteúdo do arquivo [generate_label.py](./generate_label.py) dentro da janela e salve.

## PARAMETROS

* `Input Layer` camada vetorial a ser usada como base, apenas polígonos.
* `Field name` Nome do campo a ser criado com o label novo
* `Label Prefix` Prefixo a ser usando na label da feição
* `Label Sufix` Sufixo a ser usando na label da feição
* `Ascending` Se a ordem será feita no sentido ASCENDENTE (marcado) ou DESCENDENTE (desmarcado)
* `CRS`: SRC que será usado para calculo de área, padrão é o EPSG: 31983

## CAMPOS DE SAIDA

O output terá 2 campos adicionados.

* `new_position`: recebe a nova posição da feição após a ordenação.
* `<new_label>`: Esse campo é definido pelo input __FIELD NAME__ e seu padrão é __new_label__
