# -*- coding: utf-8 -*-

from os import sep
layers = iface.legendInterface().layers()
exp = QgsExpression("""field_3 = 12.2253 or $id = 3""")
new_layers = []
root = QgsProject.instance().layerTreeRoot()
node_group = root.insertGroup(0, "DADOS_FILTRADOS")


def where(layer, exp):
    """Font https://docs.qgis.org/2.18/pt_BR/docs/pyqgis_developer_cookbook/
    expressions.html#expressions"""
    layers = list(layer.getFeatures())
    id = []
    if exp.hasParserError():
        raise Exception(exp.parserErrorString())
    exp.prepare(layer.pendingFields())
    for feature in layers:
        value = exp.evaluate(feature)
        if exp.hasEvalError():
            raise ValueError(exp.evalErrorString())
        if bool(value):
            id.append(layers.index(feature))
    return id


for layer in layers:
    # Select features in layer
    # cleaning previous selection
    layer.setSelectedFeatures([])
    layer.setSelectedFeatures(where(layer, exp))
    folder_path = str(layer.source()).split(sep)[:-1]
    file = layer.name()+"_DadoFiltrado"
    layer_out = sep.join(folder_path)+sep+file
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        QgsVectorFileWriter.writeAsVectorFormat(layer,
                                                r"{out}".format(out=layer_out),
                                                "utf-8", None, "ESRI Shapefile"
                                                , True)
        new_layers.append(layer_out)
        # print r"{saida}".format(saida=file)

for i in new_layers:
    name = i.split(sep)[-1]
    layer = QgsVectorLayer(i+".shp", name, "ogr")
    QgsMapLayerRegistry.instance().addMapLayer(layer, False)
    node_group.addLayer(layer)

print "{d} layers inserted.".format(d=len(new_layers))
