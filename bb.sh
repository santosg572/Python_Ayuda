#!/bin/bash

fil="numpy_"

i2="0"
for i in `seq 0 50 900`
do
  i2=$((i2+50))
  echo ${fil}${i}, ${i}, ${i2}
  python p3.py ${i} ${i2} > ${fil}${i}.txt
#  pandoc ${fil}${i}.txt -o ${fil}${i}.pdf
done
