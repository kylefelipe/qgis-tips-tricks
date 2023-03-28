# Created At 2021-09-21
# By Kyle Felipe At gmail.com
# Função cria um ponto em uma linha a partir de uma distância em x e y
# sendo que a distância em x é o deslocamento em relação ao início da linha, em metros
# e a distância em y é o deslocamento perpendicular à linha, em metros
# Qgis => 3.22
# Função foi criada em função da dúvida de um colega no grupo do telegram do Qgis Brasil
# https://t.me/thinkfreeqgis

from qgis.core import *
from qgis.gui import *


@qgsfunction(args='auto', group='Kyle Expressions', referenced_columns=[])
def plot_tree(dist_x,
              dist_y,
              layer_id,
              layer_field,
              value,
              side, feature, parent):
    """
    Calcula um ponto a partir de uma distância x do início de linha e uma distancia y
    perpendicular à linha.
    <h2>Parâmetros</h2>
    <table>
        <tr>
            <td>dist_x</td><td>Distância em x, em metros</td>
        </tr>
        <tr>
            <td>dist_y</td><td>Distância em y, em metros</td>
        </tr>
        <tr>
            <td>layer_id</td><td>Id da camada de linha</td>
        </tr>
        <tr>
            <td>layer_field</td><td>Campo da camada de linha com identificador único</td>
        </tr>
        <tr>
            <td>value</td><td>Valor do campo da camada de linha</td>
        </tr>
        <tr>
            <td>side</td><td>Lado do ponto em relação à linha. Escolha entre "left" ou "right"</td>
        </tr>
    </table>
    <h2>Exemplo de uso:</h2>
    <ul>
      <li>plot_tree( "x" ,  "y" , 'linhas_cb908956_f5b0_4fc0_aefe_e029d1d62837', 'fid', 1, 'right') -> geometry: Point</li>
    </ul>
    """
    # Get the line layer
    line_layer = QgsProject.instance().mapLayer(layer_id)
    # Create string expression to filter the line layer
    expression = f'"{layer_field}" = {value}'
    # create a feature request with the expression to filter the line layer
    request = QgsFeatureRequest().setFilterExpression(expression)
    # get the feature from the line layer
    line_feature = line_layer.getFeatures(request)
    line_feature = next(line_feature)
    # Get the geometry of the line feature
    geom_line = line_feature.geometry().asPolyline()
    # get the start point of the line
    start_point = geom_line[0]
    # Get the point at the distance dist_x
    interpolated_distance = line_feature.geometry().interpolate(dist_x).asPoint()
    # Calculate slope of AB
    xA, yA = start_point.x(), start_point.y()
    xB, yB = interpolated_distance.x(), interpolated_distance.y()
    slope_AB = (yB - yA) / (xB - xA)

    # Calculate slope of BC as negative reciprocal of AB
    slope_BC = -1 / slope_AB

    # Calculate x-coordinate of point C using Pythagorean theorem
    xC1 = xB + dist_y / (slope_BC ** 2 + 1) ** 0.5
    xC2 = xB - dist_y / (slope_BC ** 2 + 1) ** 0.5

    # Select the correct x-coordinate of point C
    if side == 'right':
        xC = xC1
    else:
        xC = xC2

    # Calculate y-coordinate of point C using equation of line BC
    yC = slope_BC * (xC - xB) + yB

    # Returning a geometry with the point C
    return QgsGeometry.fromPointXY(QgsPointXY(xC, yC))
