import numpy as np

mat1 = [[1, 2, 3],
        [4, 1, 2],
        [3, 1, 5]]

mat2 = [[[1, 2, 3],
         [4, 1, 2],
         [3, 1, 5]],
        [[5, 2, 3],
         [1, 1, 2],
         [3, 1, 5]],
        [[1, 4, 3],
         [4, 1, 2],
         [3, 1, 5]]]


mat2 = np.array(mat2)

print(np.amax(mat2))
print('eje 0: ', np.amax(mat2, axis=0))

print('eje 1: ', np.amax(mat2, axis=1))
