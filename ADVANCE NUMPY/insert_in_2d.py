import numpy as np

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d) 

new_arr_2d = np.insert(arr_2d,1,[5,6],axis =0) # axis = 0 row,axis = 1 coloumn

print(new_arr_2d)