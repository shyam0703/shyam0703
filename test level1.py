#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Print your name 5 times using only while loop.

a=1
while a<=5:
    print("Shyam")
    a+=1


# In[5]:


#2. Print numbers 1 to 10 using only while loop.

i=1
while i<=10:
    print(i)
    i=i+1


# In[7]:


#3. Print numbers 10 down to 1 using only while loop. 

i=10
while i>=1:
    print(i)
    i=i-1


# In[11]:


#4. Take a number from user and print its multiplication table (up to 10) using while loop.

a=eval(input("Enter the number :"))
i=1
while i<=10:
    print(a,"*" ,i ,"=" ,a*i)
    i+=1


# In[13]:


#5. Keep asking for password until user enters "analytics2025" → print "Login Success!". 

Keypin = "python2025"
pin=input("Enter your password :")
while pin!=Keypin:
    print("Enter correct pin!")
    pin=input("Enter your password :")
print("Login Success!")


# In[15]:


#6. Add numbers continuously until user enters 0, then print the sum of all entered numbers. 

sum=0
num=eval(input("Enter the value:"))
while num!=0:
    sum+=num
    num=eval(input("Enter the value:"))
print(sum)    


# In[17]:


#7. Calculate factorial of a number using only while loop (e.g., 6! = 720). 
num=eval(input("Enter the value:"))
fact=1
while num>1:
    fact*=num
    num-=1
print(fact)  


# In[19]:


#8. Reverse a number using while loop (12345 → 54321). 

num=eval(input("Enter the value:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)    


# In[21]:


#9. Number guessing game: secret = 35. Give hints "Too high"/"Too low" until correct.

Secret=int(input("Enter the value:"))

while Secret!=35:
    if Secret>35:
        print("Too high")
        Secret=int(input("Enter the value:"))
        
    else:
        print("Too low")
        Secret=int(input("Enter the value:"))
print("Secret")    


# In[25]:


#10. Check if a number is palindrome using only while loop (no string methods). 

num=int(input("Enter the value:"))
rev=0
i=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==i:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    


# In[ ]:




