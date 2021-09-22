# Created At 2021-09-21
# By Kyle Felipe At gmail.com
# Font: https://inteligenciageograficaparatodos.blogspot.com/2020/10/funcoes-customizadas-lista-de-vertices.html


from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def vetices_to_html(feat_geom, feature, parent):
    """
    Generates an html table with vertices from a given geometry
    <h2>Example usage:</h2>
    <ul>
      <li>vetices_to_html(geometry)</li>
      <li>vertices_to_html() if used at field calculator </li>
    </ul>
    """
    list_vertices = ['<table style="width:100%"  border="1"> <tr> <th>Vértice</th> <th>X</th> <th>Y</th> </tr>']
    geom = feat_geom
    if feat_geom is None:
        geom = feature.geometry()
    vertices = geom.vertices()
    for id, vertice in enumerate(vertices):
            list_vertices.append ((f'<tr> <td>{id}</td> <td>{vertice.x()}</td> <td>{vertice.y ()}</td> </tr>' ))
    list_vertices.append('</table>')
    return '\n'.join(list_vertices)
