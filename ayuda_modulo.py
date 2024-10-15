import sys
import numpy as np
import random
import turtle
import pandas as pd

dd = dir(pd)

print(len(dd))
pref = 'pd'

k = 1
for ss in dd:
  if not(ss[0] in '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    print('==========' + str(k) + '===============' + ss + '=====================')
    com = pref + '.' + ss
    res = help(eval(com))
    print(res)
    k = k+1

print(k)
