#!/bin/bash

for i in `seq 13`
do 
 n1=$((($i-1)*50+1))
 n2=$(($i*50))
 echo $n1-$n2
 python p1.py $n1 $n2 > numpy_${n1}_${n2}.txt
done



