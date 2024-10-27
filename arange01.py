import numpy as np

mat1 = [[1, 2, 3],
        [4, 1, 2],
        [3, 1, 5]]

mat = np.array(mat1)

print(np.amax(mat1))
print('eje 0: ', np.amax(mat1, axis=0))

print('eje 0: ', np.amax(mat1, axis=1))
