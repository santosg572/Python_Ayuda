import numpy as np
import math

x1 = [[1, 2, 3],
        [4, 1, 2],
        [3, 1, 5],
        [1, 6, 2]]


mat1 = np.array(x1)

print(mat1)

print(mat1.shape)

res = np.apply_along_axis(np.sum, axis=0, arr=mat1)

print(res)


res1 = np.apply_along_axis(np.sqrt, axis=1, arr=mat1)

print(res1)



