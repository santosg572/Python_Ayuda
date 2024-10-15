import sys
import numpy as np
import random
import turtle
import pandas as pd

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

def Escribe(n1=0, n2=0, pref=''):
  global DD

  k = n1
  np1 = 0
  while k <= n2:
    ss = dd[k]
    print(ss)
    if not(ss[0] in '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
      print('==========' + str(k) + '===============' + ss + '=====================')
      com = pref + '.' + ss
      res = help(eval(com))
      k = k+1
      np1 = np1+1
    else:
      k = k+1

dd = dir(pd)

nl = len(dd)
print('longitud: ', nl)


global DD
DD = dd

if n2 > nl:
  n2 = nl

Escribe(n1, n2, 'pd')



