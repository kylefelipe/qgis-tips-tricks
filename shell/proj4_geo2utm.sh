#!/bin/bash
# GPL2 by yjmenezes at gmail dot com ver 1.0 $ 2013-06-26
# exemplo de uso do proj4, entrada wgs84 lat lon graus decimais
proj +proj=utm +lon_0=51w +south +ellps=WGS84 -f "%.3f" -r << EOF
  -25.377403802778 -49.308814219444 917.219 bueiro1
  -25.3778093722 -49.30913235 919.430 prego1
EOF
# rearranjando a entrada para o proj4 com AWK
cat << EOF  | awk '{ print $3, $2, $4, $1 }' | \
  proj +proj=utm +zone=22 +south +ellps=WGS84 -f "%.3f"
  bueiro2 -25.377403802778 -49.308814219444 917.219
  prego2  -25.3778093722   -49.30913235     919.430
EOF
# +north
proj +proj=utm +lon_0=51w +north +ellps=WGS84 -f "%.3f" -r << EOF
  25.377403802778 -49.308814219444 917.219 bueiro3
  25.3778093722 -49.30913235 919.430 prego3
EOF
# rearranjando a entrada para o proj4 com AWK
cat << EOF  | awk '{ print $3, $2, $4, $1 }' | \
  proj +proj=utm +zone=22 +north +ellps=WGS84 -f "%.3f" 
  bueiro4 25.377403802778 -49.308814219444 917.219
  prego4  25.3778093722   -49.30913235     919.430
EOF

exit 0
