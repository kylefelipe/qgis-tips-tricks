# funcoes_qgis
Aqui estão contidas as funções que tenho criado para o QGIS.

Como inserir funções novas no QGIS:
Abra uma tabela de atributos e clique em "Selecionar por Expressão"
Na Janela que abrir, clique na aba "EDITOR DE FUNÇÃO"
Clique em "NEW FILE", copie o código da expressão que deseja e cole na janela do QGIS, em seguida clique em LOAD....

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
  
