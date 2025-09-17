
# loop
for i in range(10):
    print(i)

# if else
if i > 5:
    print("i is greater than 5")
else:
    print("i is less than 5")


XX =[]
for i in range(10):
    if XX % 2 == 0:
        XX.append(i)
print(XX)

XX = [i for i in range(10)]
print(XX)

# ALWAYS USE VECTOR OR MATRIX OPERATION NOT LOOP FOR PERFORMANCE REASONS


import numpy as np

# 1. Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2. Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# 3. Create a 3D array