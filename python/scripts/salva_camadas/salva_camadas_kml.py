# -*- coding: utf-8 -*-
# Author: Kyle Felipe Vieira Roberto
# E-mail: kylefelipe@gmail.com
# Date: 2018/05/22

from os import sep
layers = iface.legendInterface().layers()

for layer in layers:

    caminho = str(layer.source()).split(sep)[:-1]
    arquivo = layer.name()+"_bkp"
    saida = sep.join(caminho)+sep+arquivo
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        QgsVectorFileWriter.writeAsVectorFormat(layer, r"{saida}".format(saida=saida), "utf-8", None, "ESRI Shapefile")
        print r"{saida}".format(saida=arquivo)

