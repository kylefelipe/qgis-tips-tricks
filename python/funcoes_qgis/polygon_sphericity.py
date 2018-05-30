# -*- coding: utf-8 -*-
from math import sqrt, pi
@qgsfunction(args=2, group='Lista')
def polygon_sphericity(values, feature, parent):
    """ calcula o grau de esfericidade do poligono.
    Quanto mais proximo de 1, mais circular o vetor é, quando mais proximo de 0, mais alongada.
    AS MEDIDAS DEVEM ESTAR NA MESMA UNIDADE
<p><h4>Syntax</h4><font color="blue">relate_area_perimeter</font>(<font color="red">AREA</font>, <font color="red">perimeter</font>)</p>
<p><h4>Argument</h4> <font color="red">AREA</font> = coluna ou funçao referente a area do poligono (Exemplo: $area ).
	<p><font color="red">PERIMETER</font> = coluna ou funçao referente ao perimetro do poligono (Exemplo: $perimeter).</p>
<p><h4>Example</h4>relate_area_perimeter("$area, $perimeter)-> 0.607763480072298 </p>
	 """
    constant = 1/(4*pi)
    area, perimeter= values[0], values[1]
    return sqrt(area/(constant*(perimeter**2)))
