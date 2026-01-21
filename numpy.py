#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a 5×5 array of random integers (1–20) and replace 3rd column with 1

import numpy as np

arr = np.random.randint(1, 21, (5, 5))
arr[:, 2] = 1   
print(arr)


# In[3]:


#Create a 4×4 array (1–16) and replace diagonal with 0

arr = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(arr, 0)
print(arr)


# In[5]:


# extract sub array (rows3-5 columns 2-3)

arr = np.arange(1, 37).reshape(6, 6)
sub = arr[2:5, 1:4]
print(sub)



# In[7]:


#Extract border elements of 5×5 random array

arr = np.random.randint(1, 50, (5, 5))
border = np.concatenate([
    arr[0, :],         
    arr[-1, :],        
    arr[1:-1, 0],      
    arr[1:-1, -1]     
])
print(border)


# In[9]:


#Element-wise add, subtract, multiply, divide

a = np.random.randint(1, 10, (3, 4))
b = np.random.randint(1, 10, (3, 4))

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", a / b)


# In[11]:


#Row-wise&column-wise sum

arr = np.arange(1, 17).reshape(4, 4)

row_sum = arr.sum(axis=1)
col_sum = arr.sum(axis=0)

print("Row wise sum:", row_sum)
print("Column wise sum:", col_sum)


# In[13]:


#Mean, median, std, variance

arr = np.random.randint(1, 50, (5, 5))

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))


# In[15]:


#Normalize the 3×3 array

arr = np.arange(1, 10).reshape(3, 3)
normalized = (arr - arr.mean()) / arr.std()
print(normalized)


# In[19]:


#Add 1D array (3,) to each row of 3×3

arr = np.random.randint(1, 20, (3, 3))
v = np.array([1, 2, 3])

result = arr + v
print(result)


# In[21]:


#Subtract (4,) array from each column of 4×4
arr = np.random.randint(1, 20, (4, 4))
v = np.array([1, 2, 3, 4])

result = arr - v.reshape(4, 1)
print(result)


# In[23]:


#Determinant, Inverse, Eigenvalues

mat = np.random.randint(1, 10, (3, 3))

det = np.linalg.det(mat)
inv = np.linalg.inv(mat)
eig = np.linalg.eigvals(mat)

print("Determinant:\n", det)
print("Inverse:\n", inv)
print("Eigenvalues:\n", eig)


# In[25]:


#Matrix multiplication

a = np.random.randint(1, 10, (2, 3))
b = np.random.randint(1, 10, (3, 2))

result = a @ b
print(result)


# In[27]:


#Reshape 3×3 → (1×9) → (9×1)

arr = np.arange(1, 10).reshape(3, 3)

arr1 = arr.reshape(1, 9)
arr2 = arr.reshape(9, 1)

print(arr1)
print(arr2)


# In[29]:


#Flatten and reshape back

arr = np.random.randint(1, 50, (5, 5))
flat = arr.flatten()
new_arr = flat.reshape(5, 5)

print(new_arr)


# In[31]:


#Fancy indexing:corners

arr = np.random.randint(1, 50, (5, 5))

corners = arr[[0, 0, -1, -1], [0, -1, 0, -1]]
print(corners)


# In[34]:


#Boolean indexing: set values >10 to 10

arr = np.random.randint(1, 30, (4, 4))
arr[arr > 10] = 10
print(arr)


# In[36]:


#Structured array with name, age, weight

data = np.array([
    ('Ravi', 25, 65.5),
    ('Kiran', 22, 70.2),
    ('Asha', 30, 55.1)
], dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

sorted_data = np.sort(data, order='age')
print(sorted_data)


# In[38]:


#Structured array for points & Euclidean distance

points = np.array([(1, 2), (4, 6), (3, 8)],
    dtype=[('x', 'i4'), ('y', 'i4')])

dists = np.sqrt(points['x']**2 + points['y']**2)
print(dists)



# In[ ]:




