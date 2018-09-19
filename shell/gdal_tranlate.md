# Comandos bash para converter varios rasters a diferentes extenções

:warning: Comandos meramente ilustrativos. **Vários parâmetros dos comando  [gdal_translate](https://www.gdal.org/gdal_translate.html) foram ignorados!**

Considerando que temos vários rasters em um formato \*.asc (por exemplo) e queremos convertê-los a outro formato (no exemplo, TIFF), podemos proceder a seguinte forma:

* Criar uma variável com o path aos rasters a serem convertidos;  
* Loop para executar para cada item dessa lista o *gdal_translate*;

1) Criando variável com lista de rasters a serem convertidos:
No terminal (*bash/shell*), usaremos o comando *[find](https://www.gnu.org/software/findutils/manual/html_mono/find.html#find-Expressions)* para buscar os arquivos com padrão \*.asc e adicionaremos o resultado a uma variavel *raster*:
```
# Identifying rasters to be translated to another extention
raster="$(find . -name *.asc)"
```
O ponto positivo em se usar o comando *find* é que ele é recursivo. Ou seja **os rasters ão precisam estar numa mesma pasta. Podem estar um subpastas diferentes**

2) Ainda no *terminal* vamos usar o *for* para iterar a cada raster, e executar o comando *gdal_translate*.
O loop tem o seguinte padrão:
```
for i in lista;
  do algum_comando;
  done;
```
Como teste, podemos iterar a lista de raster e "printar" cada um deles:
```
for i in $raster;
  do echo "O raster a ser convertido é: $raster";
  done;
```
**Resultado esperado**
```
$ for i in $raster; do echo "O raster a ser convertido é: $i"; done;
O raster a ser convertido é: ./GRIP4_density_total/grip4_total_dens_m_km2.asc
O raster a ser convertido é: ./GRIP4_density_tp1/grip4_tp1_dens_m_km2.asc
O raster a ser convertido é: ./GRIP4_density_tp2/grip4_tp2_dens_m_km2.asc
O raster a ser convertido é: ./GRIP4_density_tp3/grip4_tp3_dens_m_km2.asc
O raster a ser convertido é: ./GRIP4_density_tp4/grip4_tp4_dens_m_km2.asc
O raster a ser convertido é: ./GRIP4_density_tp5/grip4_tp5_dens_m_km2.asc
```
Para a conversão, vamos remover o echo e incluir o gdal_translate. Ficando assim:
```
for i in $raster; do gdal_translate $a -a_srs EPSG:4326 -of GTiff ${i%.*}.tif; done
```
**Entendendo o comando e parâmetros usados**
Como os arquivos asc não possuem o Sistema de Referencia Cartográfica definido, vou aproveitar e definir o SRC para o output, com o comando `-a_srs EPSG:4326` onde 4326 é o id do SRC WGS84. Além disso, defino o formato de outpu com o comando `-of GTiff`.
Para informar o nome do arquivo de output, vou aproveitar a lista criada, mas precisarei remover a extensão *.asc* e inserir a extensão *.tif*. Para tanto, uso o comando `${i%.\*}.tif`
