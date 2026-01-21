#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A: Data Selection

# 1.Create a DataFramedf with 10 rows and 5 columns containing random integers from 1 to 100.
# a. Select the value at the 3rd row and 2nd column.
# b. Select all rows but only columns ['A', 'C'].
# c. Select multiple rows [2, 4, 7] and all columns.
# d. Select rows [1, 3, 5] and columns ['B', 'D'].

import numpy as np
import pandas as pd
a=np.random.randint(1,101,50)
print(a)
b=a.reshape(10,5)
print(b)
df=pd.DataFrame(b,columns=["A","B","C","D","E"])
print("DataFrame:\n",df)
a=df
print("The value at the 3rd row and 2nd column:",b[2,1])
print("all rows but only columns ['A', 'C']\n",df.loc[:,["A","C"]])
print("multiple rows [2, 4, 7] and all columns\n",df.iloc[[2,4,7],:])
print("rows [1, 3, 5] and columns ['B', 'D']\n",df.loc[[1,3,5],["B","D"]])



# In[3]:


#B: Data Modification
# 2.Using the same DataFramedf:
# a. Add a new column E with values [10,20,...] corresponding to row numbers.
# b. Remove the column C.
# c. Replace all values in column B with 0.
# d. Replace row 4 with [1,2,3,4,5].
# e. Replace rows [2,5] in column A with 99.
# f. Replace rows [0,1,2] with [ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ].
# df=df.drop(index="B")


df["E"]=[10,20,30,40,50,60,70,80,90,100]
print(df)
print("\nDataFrame After deleting column C\n",df.drop(columns="C"))
df.loc[:,"B"]=0
print("all values in column B with 0\n",df)
df.loc[3,:]=[1,2,3,4,5]
print("Replaced row 4 with [1,2,3,4,5]\n",df)
df.loc[[2,5],"A"]=99
print("Replaced rows [2,5] in column A with 99\n",df)
df.loc[[0,1,2]]=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
print("Replace rows [0,1,2] with [ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ]\n",df)
print("drop index B\n",df.drop(columns="B"))
a


# In[7]:


# C: Deleting Values
# 3.a. Delete a single value in the DataFrame by setting it to NaN.
# b. Drop row 3 entirely.
# c. Drop column D.
# d. Drop multiple columns ['B', 'E'].
# e. Drop multiple rows [0,2,5].


df.loc[5,"C"]=np.nan
print("Delete a single value in the DataFrame by setting it to NaN\n",df)
print("Drop row 3 entirely:\n",df.drop(index=2))
print("Drop row 3 entirely\n",df)
print("Drop column D:\n",df.drop(columns="D"))
print("Drop multiple columns ['B', 'E']:\n",df.drop(columns="E"))
print("Drop multiple rows [0,2,5]:\n",df.drop(index=[0,2,5]))
df



# In[9]:


#D: Mathematical Operations
# 4.	a. Add 10 to all values in column A.
# b. Multiply column B by 2.
# c. Calculate the sum of row 5.
# d. Calculate the mean of all columns.


print(df)
df["A"]+=10
print("Added 10 to all values in column A\n",df)
df["B"]*=2
print("Multiply column B by 2\n",df)
print("Calculate the sum of row 5:", df.iloc[4].sum())



# In[11]:


#E: Conditional Selection
# 5.	a. Extract all rows where column A > 50.
# b. Extract all rows where column B < 30 and column D > 10.
# c. Replace all values in column C where value < 50 with 0.

print(a)
print("Extract all rows where column A > 50\n",a[a["A"]>50])
print("Extract all rows where column B < 30 and column D > 10\n",a[(a["B"]<30) & (a["D"]>10)])
# 
# a[a.loc[:,"C"]<50]=0
a.loc[a["C"] < 20, "C"] = 0
print("Replace all values in column C where value < 20 with 0\n",a)



# In[13]:


#F: Bonus / Advanced
# 6.a. Replace multiple rows and multiple columns with a single value (e.g., replace rows [1,2] and columns ['B','D'] with 999).
# 7.b. Replace multiple rows and multiple columns with different values.
# 8.c. Extract values using iloc and loc for specific positions and labels.
print(a)
a.loc[[1,2],["B","D"]]=999
print("\nReplace multiple rows and multiple columns with a single value (e.g., replace rows [1,2] and columns ['B','D'] with 999)")
print(a)
a.loc[[1,3,5],["A","C"]]=[[1,3],[109,95],[3,5]]
print("Replace multiple rows and multiple columns with different values\n",a)
print("using loc:\n",a.loc[[1,3,7],["C","E"]])
print("using iloc:\n",a.iloc[[1,6,9]])


# In[ ]:




