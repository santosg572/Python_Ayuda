import sys
import numpy as np
import random
import turtle

#print(sys.argv[0])
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

#print(len(sys.argv))

x = dir(np)

nx = len(x)
print(nx)

for i in range(n1, n2+1):
 s = x[i]
 if not(s[0] in '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
  print('\n\nXXXXXXXXXXXXXXXXXXXXXXX ' + s + ' XXXXXXXXXXXXXXXXXXXXX\n\n')	
  com = 'np.'+s
  print(help(eval(com)))



