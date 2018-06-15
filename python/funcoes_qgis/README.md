# QGIS, tips & tricks - PYTHON - funcoes_qgis
Aqui estão contidas as funções que tenho criado para o QGIS.

Como inserir funções novas no QGIS:
Abra a calculadora de campo do QGIS e clique na aba "EDITOR DE FUNÇÃO"
Clique em "NEW FILE", copie o código da expressão que deseja e cole na janela do QGIS, em seguida clique em LOAD
A função nova irá aparecer na listagem....  
Assista ao vídeo de como inserir novas funções, feitas no python, no QGIS:  
[![Assista ao vídeo de como inserir novas funções no QGIS](https://img.youtube.com/vi/7JEcE0t70-c/0.jpg)](https://www.youtube.com/watch?v=7JEcE0t70-c)


Função verifica_valor:  
> Recebe uma lista, ou um campo que contenha uma lista, os valores devem possui um separador (virgula, dois pontos, ponto e vírgula, etc), e retorna Verdadeiro ou Falso.
  Dependencias: Não há  
  Lista de funções: "Lista"  
  Sintaxe: verifica_valor(lista, divisor, dado)
  Argumentos:  
  lista: É a lista, ou campo que conhenha uma lista.  
  separador: é o simbolo utilizado como separador (vírgula, ponto, dois pontos, ponto e vígula...) entre aspas simples ''.  
  pesquisa: é o dado que deseja procurar dentro da lista.  
  Exemplo verifica_valor('1, 2, 3, 4', ',', 1) >> True  
  OBS: É importante não utilizar letras como separador, bem como espaço e o simbolo _ (underline).  

Função padroniza_data:  
> Padroniza uma data em em um campo da tabela de atributos e retorna no formato aaaa-mm-dd, a data a ser modificada
  não contiver dia, mes e ano, a função retorna Null.  
  Dependencias: Não há  
  Lista de funções: "Date and Time"  
  Sintaxe: padroniza_data(separador, data)  
  separador: é o simbolo utilizado como separador (vírgula, ponto, dois pontos, ponto e vígula...) entre aspas simples ''.  
  data: é o data, ou campo que conten os dados de data.  
  Exemplo1 padroniza_data('/', '01/jan/2017') >> 2017-01-01  
  Exemplo2 padroniza_data('/', '01/jan') >> Null  
  OBS: É importante não utilizar letras como separador, bem como espaço e o simbolo _ (underline).  
  
Função polygon_sphericity:  
> Calcula o grau de esfericidade de um poligono, fazendo a relação entre o perimetro de um vetor com sua area e retrona um valor entre 0 e 1, sendo que quanto mais proximo a 1 mais circular é a fórma do vetor.
  Dependencias: Não Há  
  Sitnaxe: polygon_sphericity(area, perimeter)  
  area: É o campo na tabela de atributos que contem o dado de área, ou a função de calculo da área.  
  perimeter: É o campo na tabela de atributos que contém o dado de área, ou a função de calculo da área.  
  Exemplo: relate_area_perimeter($area, $perimeter) >>> 0.607763480072298  
  OBSERVAÇÃO: AMBAS MEDIDAS NECESSITAM ESTAR NA MESMA UNIDADE.  

Função wrap_delimiter:
> Quebra um texto de acordo com um delimitador
  Dependencias: Não Há
  Sitnaxe: wrap_dellimiter(string, delimiter)
  string: Texto a ser quebrado
  delimieter: É o caractere onde deve ocorrer a quebra do texto, sempre ente aspas simples.
  Exemplo: wrap-delimiter('don't panic, it will be wrapped', ',')
  don't panic
  it will be wrapped