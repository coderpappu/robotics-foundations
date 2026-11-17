from traceback import print_tb

import numpy as np

# a = np.array([1,2,3])
# print(a)
#
# b = np.array([[2,3,5,6], [7,4,3,6]])
#
# print(b)
# print(b.ndim)
# print(b.shape)
# print(b.size)
# print(b.dtype)
# print(b.itemsize)


# a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
# print(a[1, ::2])

arr = np.array([1, 2, 3, 4])
newarr = arr.astype('f')

print(newarr)

print(arr.dtype)


# check = np.full((4,5),99)
#
#
# full_like = np.full_like(arr, 10)
# print(full_like)

# rannum = np.random.rand(5, 4)
# print(rannum)

arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3, axis =0)
print(r1)





