import numpy as np

mati = [[1, 2, 3],
        [4, 1, 2],
        [3, 1, 5],
        [1, 6, 1]]

mat1 = np.array(mati)

print(mat1.shape)

e1 = np.array([[1,2,3,4]])
e0 = np.array([[3,2,1]])

print(e0.shape)
print(e1.shape)

mat2 = np.append(mat1, e0, axis=0)

print('APPEND 0')
print(mat2)

print('ORIGINAL')
print(mat1)

mat3 = np.append(mat1, e1, axis=1)
print('APPEND 1')
print(mat3)



