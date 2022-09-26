# Criado por Kyle Felipe
# Data: 2022/09/16
# Esse script foi criado para que as funções do QGIS do usuário sejam registadas
# na inicialização do programa.
# Faça os imports necessários da sua função e coloque-a nesse script e insira o
# nome da função na tupla functions_to_load
# esse arquivo pode ser colocado nas pastas indicadas pela documentação do QGIS
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/intro.html?highlight=startup#running-python-code-when-qgis-starts
# o nome do arquivo precisa ser startup.py, pois é o nome que o QGIS vai procurar

from qgis.utils import qgsfunction

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Hebert Azevedo')
def retira_acento(value1, feature, parent):
    """Função criada por Herbert Azevedo
    https://groups.google.com/g/qgisbrasil/c/nzP3gfJo5KM
    """
    
    listaa = 'àáâãäèéêëìíîïòóôõöùúûüÀÁÂÃÄÈÉÊËÌÍÎÒÓÔÕÖÙÚÛÜçÇñÑ '
    
    listab = 'aaaaaeeeeiiiiooooouuuuAAAAAEEEEIIIOOOOOUUUUcCnN '
    
    k = 0
    
    for caract in listaa:
        value1 = value1.replace(caract, listab [k])
        k += 1

    return value1

functions_to_load = (retira_acento,)

def registerFunction(isRegister=True):
    """Registra as funções para uso no qgis"""
    for f in functions_to_load:
        QgsExpression.registerFunction(f)    

registerFunction()
