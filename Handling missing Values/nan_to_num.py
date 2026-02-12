# np.nan_to_num(array, nan=value) defualt - 0

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])

print(np.isnan(arr))

cleaned_arr = np.nan_to_num(arr,nan=100) # if u pass nothing defualt value would be zero 
print(cleaned_arr)