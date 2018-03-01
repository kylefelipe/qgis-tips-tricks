# QGIS, tips & tricks - PYTHON - funcoes_qgis
Aqui estão contidas as funções que tenho criado para o QGIS.

Como inserir funções novas no QGIS:
Abra a calculadora de campo do QGIS e clique na aba "EDITOR DE FUNÇÃO"
Clique em "NEW FILE", copie o código da expressão que deseja e cole na janela do QGIS, em seguida clique em LOAD
A função nova irá aparecer na listagem....

Função verifica_valor:
  Recebe uma lista, ou um campo que contenha uma lista, os valores devem possui um separador (virgula, dois pontos, ponto e vírgula, etc),
  e retorna Verdadeiro ou Falso.
  Dependencias: 
  Lista de funções: "Lista"
  Sintaxe: verifica_valor(lista, divisor, dado)
  Argumentos:
  lista: É a lista, ou campo que conhenha uma lista.
  separador: é o simbolo utilizado como separador (vírgula, ponto, dois pontos, ponto e vígula...) entre aspas simples ''.
  pesquisa: é o dado que deseja procurar dentro da lista.
  Exemplo verifica_valor('1, 2, 3, 4', ',', 1) >> True
  OBS: É importante não utilizar letras como separador, bem como espaço e o simbolo _ (underline).

Função padroniza_data:
  Padroniza uma data em em um campo da tabela de atributos e retorna no formato aaaa-mm-dd, a data a ser modificada
  não contiver dia, mes e ano, a função retorna Null.
  Dependencias:
  Lista de funções: "Date and Time"
  Sintaxe: padroniza_data(separador, data)
  separador: é o simbolo utilizado como separador (vírgula, ponto, dois pontos, ponto e vígula...) entre aspas simples ''.
  data: é o data, ou campo que conten os dados de data.
  Exemplo1 padroniza_data('/', '01/jan/2017') >> 2017-01-01
  Exemplo2 padroniza_data('/', '01/jan') >> Null
  OBS: É importante não utilizar letras como separador, bem como espaço e o simbolo _ (underline).
  
