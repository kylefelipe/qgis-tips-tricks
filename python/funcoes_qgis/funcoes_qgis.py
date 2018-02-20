@qgsfunction(args=3, group='Lista')
def verifica_valor(values, feature, parent):
    """Retorna verdadeiro se um valor encontra-se dentro da lista, caso contrario, falso.
<p><h4>Syntax</h4><font color="blue">verifica_valor</font>(<font color="red">lista</font>, <font color="red">separador</font>,<font color="red"> pesquisa</font>)</p>
<p><h4>Argument</h4> <font color="red">LISTA</font> = coluna onde encontra-se a lista de valores (Exemplo: "campo").
	<p><font color="red">SEPARADOR</font> = simbolo do separador da lista(Exemplo: ',').</p>
	<p><font color="red">PESQUISA</font> = Valor procurado dentro da coluna.</p>
<p><h4>Example</h4>verifica_valor("campo", ',',5)-> "5, 4, 6, 1" -> 5 -> TRUE </p>
	 """
	 
    str_lista, separador, pesquisa = values[0], values[1], values[2]
    return str(pesquisa) in str_lista.replace(" ", "").split(separador)
