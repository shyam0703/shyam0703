#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

a={x: x**2 for x in range(1,11)}
print(a,type(a))



# In[3]:


#2.Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

print("value of 5:",a[5])
print("keys of the dictionary:", a.keys())


# In[34]:


#3.Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. 
#Print the modified dictionary.

a[11]=121
print(a)


# In[36]:


#4.Iterate over the dictionary created in Assignment 1 and print each key-value pair.

for k,v in a.items():
    print(k,"==>",v)


# In[38]:


#5.Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. 
#Print the new dictionary.

b={x: x**3 for x in range(1,11)}
print(b)


# In[40]:


#6.Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as 
#the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

a={x: x**2 for x in range(1,6)}
b={x: x**2 for x in range(6,11)}
print(a)
print(b)
a.update(b)
print(a)


# In[42]:


#7.Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' 
#is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

a={"name":"Jeji","age":21,"grades":{"maths":"A","science":"A","english":"O"}}
print(a,type(a))


# In[44]:


#8.Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples
#of the key. Print the dictionary.

a={x:[x*y for y in range(1,6)]for x in range(1,6)}
print(a,type(a))



# In[46]:


#9.Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its 
#square.Print the dictionary.

a={x:(x,x*x) for x in range(1,6)}
print(a)


# In[48]:


#10Create a dictionary with the first 5 positive integers as keys and their squares as values.
#Convert the dictionary to a list of tuples and print it.

a={x: x**2 for x in range(1,6)}
print(a)
b=list(a.items())
print(b,type(b))


# In[50]:


#11.Create a dictionary with the first 10 positive integers as keys and their squares as values. 
#Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

a={x: x**2 for x in range(1,11)}
print(a)
even={k: v for k,v in a.items() if k%2 == 0}
print(even)


# In[52]:


#12.Create a dictionary with the first 5 positive integers as keys and their squares as values. 
#Create a new dictionary with keys and values swapped. Print the new dictionary.

a={x: x**2 for x in range(1,6)}
sw={v: k for k,v in a.items()}
print(a)
print(sw)


# In[54]:


#13.Create a default dictionary where each key has a default value of an empty list. 
#Add some elements to the lists and print the dictionary.

a={}
print(a,type(a))
a.setdefault('a',[]).append(1)
a.setdefault('a',[]).append(10)
a.setdefault('c',[]).append(51)
a.setdefault('d',[]).append(100)
print(a)



# In[58]:


#14.Write a function that takes a string and returns a dictionary with the count of each character in the string. 
#Print the dictionary.

a={1:"shyam"}
for k,v in a.items():
    print(a,type(a),type(v))
   


# In[ ]:




