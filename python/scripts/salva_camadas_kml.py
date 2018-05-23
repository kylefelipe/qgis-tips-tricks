# -*- coding: utf-8 -*-
# Author: Kyle Felipe Vieira Roberto
# E-mail: kylefelipe@gmail.com
# Date: 2018/05/22

from os import sep
layers = iface.legendInterface().layers()

for layer in layers:

    caminho = str(layer.source()).split(sep)[:-1]
    arquivo = layer.source()[:-4]+".kml"
    saida = sep.join(caminho)+sep+arquivo
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        QgsVectorFileWriter.writeAsVectorFormat(layer, r"{saida}".format(saida=arquivo), "utf-8", None, "KML")
        print r"{saida}".format(saida=arquivo)
        
