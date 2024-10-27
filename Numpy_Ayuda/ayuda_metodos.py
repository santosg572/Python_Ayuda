import numpy as np

'''
lista = ['amax', 'append', 'apply_along_axis', 'arange', 'argmax', 'around', 'array', 'bartlett', 'c_',
         'char', 'choose', 'concatenate', 'copy', 'corrcoef', 'cos', 'cumsum', 'delete', 'diff',
         'dot', 'e']


lista = ['emath', 'empty', 'exp', 'eye', 'fft', 'flip',  'fmax', 'gcd', 'gradient', 'histogram', 
          'hsplit', 'i0', 'imag', 'indices', 'isin', 'iterable', 'ix_', 'lcm', 'linspace', 'load', 'log10']


lista = ['logical_and', 'logspace', 'lookfor', 'mat', 'mean', 'meshgrid', 'mod', 'moveaxis', 'nan', 'nanmin',
         'ndarray', 'ndim', 'numarray', 'percentile', 'poly', 'polyder', 'polyfit', 'polyval', 'quantile',
         'random', 'rec', 'repeat', 'reshape', 'roll']

'''
lista = ['roots', 'save', 'select', 'shape', 'single', 'size', 'source', 'split', 'take', 'tensordot', 
         'transpose', 'vdot', 'where', 'who']


print(len(lista))

for ss in lista:
  com = 'np.'+ss
  print(help(eval(com)))

