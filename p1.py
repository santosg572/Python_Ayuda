import sys
import numpy as np
import random
import turtle

x = dir(turtle)

nx = len(x)

print(nx)

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print((n1, n2))

for i in range(n1, n2):
 s = x[i]
 if s[0] != '_':
  print('\n\nXXXXXXXXXXXXXXXXXXXXXXX ' + s + ' XXXXXXXXXXXXXXXXXXXXX\n\n')	
  com = 'turtle.'+s
  print(help(eval(com)))



