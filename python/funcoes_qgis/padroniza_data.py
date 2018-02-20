@qgsfunction(args=2, group='Date and Time')
def padroniza_data(values, feature, parent):
    """padroniza as datas de um campo do qgis para o seguinte formato aaaa-mm-dd.
    <p><h4>Syntax</h4><font color="blue">padroniza_data</font>(<font color="red">separador</font>,<font color="red">data</font>)
    <p><font color="red">SEPARADOR</font> = simbolo separador utilizado na data que está errada (Exemplo: ',').</p>
    <p><font color="red">DATA</font> = Valor de data ou o campo com a data errada.</p>
    <p><h4>Example</h4>padroniza_data('/', "01/jan/2017 )-> 2017-01-01</p>
    """
    meses = {'JANEIRO': '01', 'FEVEREIRO': '02', 'MARÇO': '03', 'ABRIL': '04', 'MAIO': '05', 'JUNHO': '06',
             'JULHO': '07', 'AGOSTO': '08', 'SETEMBRO': '09', 'OUTUBRO': '10', 'NOVEMBRO': '11', 'DEZEMBRO': '12'}
    str_data = str(values[1])
    if len(str_data.split(values[0])) == 3:
        dia, mes, ano = str_data.split(values[0])
        if str.isdigit(mes.encode("utf8")) is False:
            for i in meses.iterkeys():
                if mes[:3].upper() == i[:3]:
                    return "{ano}-{mes}-{dia:02d}".format(ano=ano, mes=meses[i], dia=int(dia))
        else:
            return "{ano}-{mes:02d}-{dia:02d}".format(ano=ano, mes=int(mes), dia=int(dia))
    else:
        return "Null"
