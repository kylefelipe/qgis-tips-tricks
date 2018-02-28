#!/bin/bash
#GPL2 by yjmenezes at gmail dot com ver 1.0 2014-09-29
# exemplo de linha de comando para interpolar DTM dada uma nuvem X Y Z
# ver 1.1 2017-03-14 filtrando Altitudes negativas com awk
# http://www.gdal.org/grid_tutorial.html  Thx Frank Wanerdan !
rm -r /tmp/grid
mkdir -p /tmp/grid
echo "processamento em /tmp/grid" 1>&2
cd /tmp/grid
echo "exemplo: criando a nuvem de pontos, entrada tipica " 1>&2
sleep 1
cat << EOF | awk -F\, 'NR == 1 || $4 > 0 { print  }'> nuvem3d.csv
Ponto,X_e84,Y_n84,Altitude
4xxx,687091.302,7155418.977,-9782
4a,687124.000,7155353.000,101.25
4b,687113.950,7155353.017,102.34
4c,687084.497,7155355.534,107.48
4d,687089.976,7155376.635,98.34
4e,687095.562,7155392.043,103.14
4f,687090.302,7155410.613,97.23
4g,687060.338,7155411.855,99.46
4h,687045.285,7155417.977,105.24
4x,687090.302,7155417.977,-9782
4i,687038.536,7155449.391,103.78
4j,687084.365,7155464.227,98.87
4k,687190.263,7155492.394,106.45
4xx,687091.302,7155417.977,-9782
4l,687213.991,7155485.218,103.68
4m,687154.991,7155449.926,105.49
4n,687182.015,7155427.091,97.65
4o,687124.371,7155424.328,99.32
EOF
# passo 1: nome das colunas deve ser coerente com a linha header da nuvem3d.csv
echo "1- criando virtual driver GDAL" 1>&2
sleep 1
cat << EOF > nuvem3d.vrt
<OGRVRTDataSource>
    <OGRVRTLayer name="nuvem3d">
        <SrcDataSource>nuvem3d.csv</SrcDataSource> 
    <GeometryType>wkbPoint</GeometryType> 
    <GeometryField encoding="PointFromColumns" x="X_e84" y="Y_n84" z="Altitude" /> 
    </OGRVRTLayer>
</OGRVRTDataSource>
EOF
echo "veja os limites z " 1>&2
grep -iv ponto nuvem3d.csv  | sort -t\, -n -k 4
echo "veja os limites x " 1>&2
grep -iv ponto nuvem3d.csv  | sort -t\, -n -k 2
echo "veja os limites y " 1>&2
grep -iv ponto nuvem3d.csv  | sort -t\, -n -k 3
#
echo "2- interpolando e gerando raster, ( moldura txe tye ) definida abaixo" 1>&2
sleep 1
gdal_grid -zfield "Altitude" -a invdist:power=2.0:smoothing=1.0 -txe 687000 687250 -tye 7155300 7155500 -outsize 250 200 -of GTiff -ot Float64 -l nuvem3d nuvem3d.vrt dem.tiff --config GDAL_NUM_THREADS ALL_CPUS
echo "3- interpolando curvas de nivel 1m" 1>&2
sleep 1
gdal_contour -a elev dem.tiff contour.shp -i 1.0
exit 0
