# $ GPL2 by yjmenezes at gmail dot com ver 1.0  2013-12-09 $
# semi_eixo, achatamento, latitude graus decimais com sinal algebrico
# calcula os raios de curvatura de secao meridiana (m)  e primeiro vertical (v )
awk 'function raio_curv(a_elip,f,lat_ddeg) {
  if ( f > 1.0) {  f = 1.0 / f };
  lat = atan2(0, -1) * lat_ddeg
  s2 = sin(lat) * sin(lat);
  e2  = f * ( 2.0 - f);
  v = 1.0 - e2 * s2;
  m = ((1.0 - e2) * a_elip) / exp(1.5 * log(v));
  v = a_elip / sqrt(v);
  printf "%.2f ", sqrt(m * v); 
} { raio_curv($1,$2,$3); printf("\n"); }'
# chamada da funcao lendo a entrada padrao e processando para saida padrao
# echo  "6378137.0   298.257223563  -31.767"  | ./raio_curv.awk 
# echo  "6378137.0   298.257223563  -31.767"  | ./raio_curv.awk | awk '{ print "arco_1km_ddeg=", 1000 / $1 * 180 / atan2(0, -1) }'
