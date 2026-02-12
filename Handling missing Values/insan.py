import numpy as np

arr = np.array([1,2,np.nan,4 ,np.nan,6]) # np.nan is considered as missing value to perform according operations

print(np.isnan(arr)) # now it will show values which are missing

# no we cannot compare it directly
# print(np.nan == np.nan)