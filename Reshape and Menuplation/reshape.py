# reshape (rows,coloumns) spacify new shape if dimension match

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshape_arr = arr.reshape(2,3)
print(reshape_arr)