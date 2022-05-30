###############################################################################
## Reordena vertices
## É necessário que haja uma camada de poligonos ativa
## e um vetor selecionado na camada
## Criado por Kyle Felipe
## kylefelipe at gmail.com
## Criado em 2022/05/30
###############################################################################

layer = iface.activeLayer()
features = layer.getSelectedFeatures()

# Criando uma camada temporária para receber os vértices
tempVp = QgsVectorLayer(f"Point?crs={layer.crs().authid()}", "temporary_points", "memory")
QgsProject.instance().addMapLayer(tempVp)
dpTempVp = tempVp.dataProvider()

id_vertex = 2 # Edite aqui ID do Vértice onde deseja iniciar a ordenação
topo = 'T' # Edite aqui o texto que deseja que vá antes do nome do número do vérice

# Criando campo para receber nome do vértice e o tipo do vérice

campos = [QgsField('toponimia', QVariant.String), QgsField('tipo', QVariant.String)]
tempVp.dataProvider().addAttributes(campos)
tempVp.updateFields()

def ordenaPoligono(pol, id_escolhido=0):
    """Essa função reordena os vertices e retorna uma nova lista"""
    return pol[id_escolhido:] + pol[1: id_escolhido]
    
    
for f in features:
    # pegando a geometria da feição
    geom = f.geometry()
    polygon = geom.asPolygon()
    ordered = ordenaPoligono(polygon[0], id_vertex)
    # Adicionando os pontos na camada temporária criada anteriormente
    for i in ordered:
        feicaoPonto = QgsFeature(tempVp.fields())
        feicaoPonto.setGeometry(QgsGeometry.fromPointXY(i))
        attributos = [f"{topo}{ordered.index(i)}"]
        feicaoPonto.setAttributes(attributos)
        dpTempVp.addFeature(feicaoPonto)


tempVp.updateExtents()
print("Terminado")
