import sys
import numpy as np
import random
import turtle

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

dd = dir(turtle)

nl = len(dd)
print(nl)

global DD

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

Escribe(n1, n2, 'turtle')



