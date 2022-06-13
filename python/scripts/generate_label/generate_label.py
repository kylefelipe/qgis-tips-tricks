# Created By kyle felipe
# Contact kylefelipe at gmail.com
# Created At: 2022 - 06 - 13

# A camada a ser usada como base precisa estar ativa (selecionada) no painel de
# camadas

virtual_layer_name = 'nova_camada_virtual' #Nome da camada virtual a ser gerada
new_column = 'rotulo' # Nome do campo novo
prefix = 'A - ' # prefixo do campo novo - esta linha nao pode ser removida
sufix = '' # Sufixo - esta linha nao pode ser removida
dest_EPSG = 31983

project = QgsProject.instance()
v_layer_id = QgsExpressionContextUtils.projectScope(project).variable('v_layer_id')

# Remove a camada virtual, caso  ja tenha sido criada
if v_layer_id:
    project.removeMapLayer(v_layer_id)

# Pega a camada ativa como base
origin = iface.activeLayer()


SQL = f"""SELECT l.*, '{prefix}' || """
SQL += f"""row_number() OVER( ORDER BY area(ST_transform(l.geometry, {dest_EPSG})) ASC )"""
SQL += f"""|| '{sufix}' as {new_column}"""
SQL += f""" FROM "{origin.id()}" as l;"""
dest_vector = QgsVectorLayer(f"?query={SQL}", virtual_layer_name, "virtual" )
QgsProject.instance().addMapLayer(dest_vector)
QgsExpressionContextUtils.setProjectVariable(project, 'v_layer_id', dest_vector.id())
