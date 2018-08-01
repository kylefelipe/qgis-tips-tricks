#!/bin/bash
# GPL2 by yjmenezes at gmail.com versao 1.0
# cloud point rotation arround a pivot point.
# depends: bc - An arbitrary precision calculator language
if [ $# -lt 1 ]
then
    echo $(basename $0)" < inputfile.pxyz  rot_ang_ddeg_with_sinal  [px] [py]" 1>&2
    echo "px,py=pivot coordinates  +CW, -CCW" 1>&2
    exit 1
fi
pi_=$(echo "scale=10; 4*a(1)" | bc -l)
alfa_rad_=$(echo "$1 * $pi_ / 180.0 " | bc -l)
si=$(echo "s($alfa_rad_)" | bc -l)
co=$(echo "c($alfa_rad_)" | bc -l)
if [ $# -ge 3 ]
then 
    px=$2
    py=$3
else
    px=0.0
    py=0.0
fi
echo $1 $px $py $alfa_rad_ $pi_ $si $co 1>&2
cat << EOF > test.pxyz
a 1 1 1
b 2 2 2
c 3  3 3
EOF
# filter comments and process input file
# si co px py pto x y z
#cat test.pxyz | grep -v \# | while read lin; do
grep -v -e ^$ -e \# | while read lin; do
    echo $si $co $px $py $lin | \
    awk '{ printf "%s\t%.3f\t%.3f\t%.3f\n", $5, (($6-$3) * $2 - ($7-$4) * $1) + $3, (($6-$3) * $1 + ($7-$4) * $2) + $4, $8 }'
done
exit 0
