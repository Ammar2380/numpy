# np.sinf(array) 10*1000
# 1/0

import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6]) # np.inf refers infinity or large value in data
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=1000, neginf=-100)
print(cleaned_arr)