```md 
Prompting: Create a comprehensive NumPy basics and practice guide for you. This will cover the fundamentals along with practical exercises to help you master NumPy.
```
# NumPy Basics and Practice Guide

## Introduction
NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these arrays.

## Installation
```bash
pip install numpy
```

## 1. NumPy Basics

### Importing NumPy
```python
import numpy as np
```

### Creating Arrays

#### From Python Lists
```python
# 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

#### Using Built-in Functions
```python
# Array of zeros
zeros = np.zeros((3, 4))  # 3x4 matrix of zeros

# Array of ones
ones = np.ones((2, 3))  # 2x3 matrix of ones

# Identity matrix
identity = np.eye(4)  # 4x4 identity matrix

# Array with range of values
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Array with evenly spaced values
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Random arrays
random_arr = np.random.random((3, 3))  # 3x3 random values [0, 1)
random_int = np.random.randint(0, 10, size=(3, 4))  # 3x4 random integers
```

## 2. Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)     # (2, 3) - dimensions
print(arr.size)      # 6 - total elements
print(arr.ndim)      # 2 - number of dimensions
print(arr.dtype)     # int64 - data type
print(arr.itemsize)  # 8 - bytes per element
```

## 3. Array Indexing and Slicing

### Basic Indexing
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])    # 1
print(arr[-1])   # 5

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])   # 1
print(arr2d[1, 2])   # 6
print(arr2d[-1, -1]) # 9
```

### Slicing
```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[2:7])     # [2, 3, 4, 5, 6]
print(arr[::2])     # [0, 2, 4, 6, 8] - every 2nd element
print(arr[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse

# 2D slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2, 1:])  # [[2, 3], [5, 6]]
print(arr2d[:, 1])    # [2, 5, 8] - second column
```

### Boolean Indexing
```python
arr = np.array([1, 2, 3, 4, 5, 6])
mask = arr > 3
print(arr[mask])  # [4, 5, 6]

# Direct boolean indexing
print(arr[arr % 2 == 0])  # [2, 4, 6] - even numbers
```

## 4. Array Operations

### Arithmetic Operations
```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
print(a + b)    # [6, 8, 10, 12]
print(a - b)    # [-4, -4, -4, -4]
print(a * b)    # [5, 12, 21, 32]
print(a / b)    # [0.2, 0.333, 0.428, 0.5]
print(a ** 2)   # [1, 4, 9, 16]
```

### Broadcasting
```python
# Broadcasting allows operations between arrays of different shapes
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print(arr + scalar)  # Adds 10 to each element

# Broadcasting with different shaped arrays
arr1 = np.array([[1, 2, 3]])  # shape (1, 3)
arr2 = np.array([[1], [2]])   # shape (2, 1)
print(arr1 + arr2)  # Result shape (2, 3)
```

## 5. Array Manipulation

### Reshaping
```python
arr = np.arange(12)
reshaped = arr.reshape(3, 4)  # 3x4 matrix
reshaped2 = arr.reshape(2, -1)  # -1 means "infer dimension"

# Flatten arrays
flattened = reshaped.flatten()
raveled = reshaped.ravel()  # Similar but returns view when possible
```

### Stacking and Splitting
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking
vstacked = np.vstack((a, b))  # Vertical stack
hstacked = np.hstack((a, b))  # Horizontal stack

# Splitting
arr = np.arange(16).reshape(4, 4)
vsplit = np.vsplit(arr, 2)  # Split into 2 arrays vertically
hsplit = np.hsplit(arr, 2)  # Split into 2 arrays horizontally
```

## 6. Mathematical Functions

### Statistical Functions
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(np.mean(arr))        # 5.0 - mean
print(np.median(arr))      # 5.0 - median
print(np.std(arr))         # Standard deviation
print(np.var(arr))         # Variance
print(np.min(arr))         # 1 - minimum
print(np.max(arr))         # 9 - maximum
print(np.sum(arr))         # 45 - sum
print(np.cumsum(arr))      # Cumulative sum

# Along specific axis
print(np.sum(arr, axis=0))  # Sum columns
print(np.sum(arr, axis=1))  # Sum rows
```

### Mathematical Operations
```python
arr = np.array([0, 30, 45, 60, 90])

# Trigonometric
print(np.sin(np.deg2rad(arr)))
print(np.cos(np.deg2rad(arr)))

# Exponential and logarithmic
print(np.exp([1, 2, 3]))
print(np.log([1, 2.718, 10]))
print(np.log10([1, 10, 100]))

# Rounding
arr = np.array([1.23, 2.47, 3.56, 4.89])
print(np.round(arr))    # Round to nearest integer
print(np.floor(arr))    # Round down
print(np.ceil(arr))     # Round up
```

## 7. Linear Algebra

```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
dot_product = np.dot(A, B)
# or
dot_product = A @ B

# Transpose
transpose = A.T

# Determinant
det = np.linalg.det(A)

# Inverse
inverse = np.linalg.inv(A)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
```

## Practice Exercises

### Exercise 1: Array Creation and Manipulation
```python
# 1. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
# Hint: Use np.eye and indexing

# 2. Create a 8x8 checkerboard pattern using 0s and 1s
# Hint: Use slicing with step

# 3. Normalize a 5x5 random matrix (values between 0 and 1)
# Formula: (X - min) / (max - min)
```

### Exercise 2: Statistical Operations
```python
# 1. Generate array of 100 random numbers from normal distribution
# Calculate mean, median, std deviation

# 2. Create a 4x4 array with random values and find:
#    - Row-wise minimum
#    - Column-wise maximum
#    - Overall mean

# 3. Find indices of non-zero elements from [1,2,0,0,4,0]
```

### Exercise 3: Array Manipulation
```python
# 1. Convert a 1D array of 12 elements into a 3D array of shape (2,3,2)

# 2. Stack two arrays vertically and then split them back

# 3. Create two 3x3 arrays and concatenate them:
#    - Horizontally
#    - Vertically
```

### Exercise 4: Boolean Indexing and Filtering
```python
# 1. From array [1,2,3,4,5,6,7,8,9,10]:
#    - Extract all even numbers
#    - Extract all numbers greater than 5
#    - Replace all odd numbers with -1

# 2. Create a 5x5 array and:
#    - Replace all values > 0.5 with 1
#    - Replace all values <= 0.5 with 0
```

### Exercise 5: Broadcasting
```python
# 1. Add a 1D array of shape (3,) to a 2D array of shape (3,3)

# 2. Multiply each row of a 5x3 matrix by a 1D array of 3 elements

# 3. Standardize each column of a 4x3 matrix (subtract mean, divide by std)
```

### Exercise 6: Advanced Operations
```python
# 1. Find common values between two arrays

# 2. Get positions where elements of two arrays match

# 3. Create a 5x5 matrix with row values ranging from 0 to 4

# 4. Find unique values and their counts in an array

# 5. Compute moving average of window size 3 for array [1,2,3,4,5,6,7,8,9,10]
```

## Solutions to Exercises

### Exercise 1 Solutions
```python
# 1. Matrix with values below diagonal
Z = np.diag(np.arange(1, 5), k=-1)

# 2. Checkerboard pattern
Z = np.zeros((8,8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1

# 3. Normalize matrix
Z = np.random.random((5,5))
Znorm = (Z - Z.min()) / (Z.max() - Z.min())
```

### Exercise 2 Solutions
```python
# 1. Normal distribution stats
Z = np.random.normal(0, 1, 100)
print(f"Mean: {np.mean(Z)}, Median: {np.median(Z)}, Std: {np.std(Z)}")

# 2. Row and column operations
Z = np.random.random((4,4))
row_min = np.min(Z, axis=1)
col_max = np.max(Z, axis=0)
overall_mean = np.mean(Z)

# 3. Non-zero indices
arr = np.array([1,2,0,0,4,0])
indices = np.nonzero(arr)[0]
```

### Exercise 3 Solutions
```python
# 1. Reshape 1D to 3D
arr = np.arange(12)
arr_3d = arr.reshape(2, 3, 2)

# 2. Stack and split
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
stacked = np.vstack((a, b))
split = np.vsplit(stacked, 2)

# 3. Concatenation
a = np.random.random((3,3))
b = np.random.random((3,3))
h_concat = np.hstack((a, b))
v_concat = np.vstack((a, b))
```

## Tips and Best Practices

1. **Use vectorized operations** instead of loops for better performance
2. **Avoid copying arrays** unnecessarily - use views when possible
3. **Specify dtype** when creating arrays if precision matters
4. **Use broadcasting** to avoid creating unnecessary large arrays
5. **Profile your code** with large datasets to identify bottlenecks
6. **Remember that NumPy arrays are mutable** - be careful with references
7. **Use np.allclose()** for floating-point comparisons
8. **Leverage NumPy's built-in functions** before writing custom implementations

## Common Pitfalls to Avoid

- Not understanding the difference between views and copies
- Forgetting that NumPy uses 0-based indexing
- Misunderstanding broadcasting rules
- Not specifying axis parameter in reduction operations
- Using Python loops instead of vectorized operations

## Next Steps

After mastering these basics, explore:
- **Pandas**: Built on NumPy for data analysis
- **SciPy**: Scientific computing extensions
- **Matplotlib**: Visualization with NumPy arrays
- **Scikit-learn**: Machine learning with NumPy
- **Advanced indexing**: Fancy indexing and advanced slicing techniques
- **Memory layout**: Understanding C vs Fortran order
- **Custom ufuncs**: Creating your own universal functions