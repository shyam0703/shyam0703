#!/usr/bin/env python
# coding: utf-8

# In[1]:


#14.Print only odd numbers from 1 to 20 using while loop and continue statement. 

i=1
while i<=20:
   if i%2==0:
       i+=1
       continue
   print(i)

   i+=1



# In[3]:


#12. Implement a login system with maximum 3 attempts. If password is wrong 3 times → 
#print "Account Blocked!". Correct password: "python123"
pin=input("Enter the password:")
password="python123"
n=0
while n<2 and password!=pin:
   print("Invalid password!,,enter correct password")
   pin=input("Enter the password:")
   n+=1
if n!=0 and password!=pin:
   print("Account Blocked!")
else:
   print("Login successful!")


# In[5]:


#13.Keep taking expense amounts until user enters -1, then print total expense and count of transactions. 

expense=eval(input("Enter the amount:"))
total=0
count=0
while expense!=-1:
    total+=expense
    count+=1
    expense=eval(input("Enter the amount:"))
print("The total expense:",total ,"\ncount of transactions:",count)    
    


# In[7]:


#14.Print only odd numbers from 1 to 20 using while loop and continue statement. 

i=1
while i<=20:
   if i%2==0:
       i+=1
       continue
   print(i)

   i+=1



# In[9]:


#15. Write a program using while loop to count and print the number of digits in a given positive integer (Example: 7834 → 4 digits).

num = int(input("Enter the value:"))
count=0
if num<0:
    print("Enter any positive value:")
while num>0:
    count+=1
    num=num//10
    
print("num of digits:",count)    


# In[13]:


# 16. (Updated) Write a program using while loop to calculate and print the sum of the series: 1 
# + 4 + 9 + 16 + … + 100 (i.e., sum of squares of first 10 natural numbers).

sum=0
i=1
while i<=10:
    sum+=i**4
    i+=1
print(sum)


# In[21]:


#17. Print first 10 Fibonacci numbers using only while loop (0, 1, 1, 2, 3, 5, …). 

i=1
a,b=0,1
print(a,b,end=" ")
while i<11:
    print(a+b,end=" ")
    a,b=b,a+b
    
    i+=1


# In[23]:


#18. Use break when user types "stop" (case insensitive) in an infinite input loop.

type=input("Enter the Value:")
while type!="stop":
    type=input("Enter the Value:")
print(type)    


# In[25]:


# 19. What is the output?Python,i = 0,while i < 3:print("Hi"),i += 1,else:print end

i=0
while i<3:
    print("Hi")
    i+=1
else:
    print("End")


# In[27]:


#20. Write a program to find GCD of two numbers using while loop (Euclidean algorithm). 

num1=int(input("Enter the first value:"))
num2=int(input("Enter the second value:"))
if num1>num2:
    i=num1
else:
    i=num2

gcd=1
j=1
while j<=1:
    if num1%j==0 and num2%j==0:
        gcd=1
    j+=1    
print(f'gcd of {num1} and {num2}:{gcd}')        



# In[ ]:




