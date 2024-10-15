#!/bin/bash

for i in `seq 1 10 170`
do 
 n1=$i
 n2=$(($i+10))
 echo $n1 ' ---- ' $n2
 python despliega_ayuda.py $n1 $n2 > "pandas_"${n1}"_"${n2}.txt
done



