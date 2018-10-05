# QGIS, tips & tricks - PYTHON - change_encode

### Autor: Kyle Felipe
### Data: 05/10/2018

Faz download das imagens LANDSAT 5, 7 e 8 do repositório do Google

Pode ser utilizado no _Python 2_ ou superior, e é necessária a instalação dos pacotes listados no requirements.txt.  
pip install -r requirements.txt

## Modo de uso

path_row = Uma lista com o path (orbita) e o Row (ponto) das images que desejam baixar no seguinte formato:  
            [(path, row), ...]  
data_inicial = Iincio do periodo que deseja fazer o download, no formato AAAA-MM-DD.  
data_final = Final do periodo que deseja fazer o download, no formato AAAA-MM-DD.  
cloud = Quantidade do percentual maximo de núvem desejado em cada imagem.  
image_folder = local onde as imagens serão baixadas, ente "".  
satellite_n = Número do satélite LANDSAT que deseja as imagens. EX: 8.
