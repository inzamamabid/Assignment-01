#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("hello, world")


# In[3]:


thankx="Thanks For Your Support"
print(thankx)


# In[ ]:





# In[ ]:


# Every element of array can be accessed with 2 type of incdices positive index or negative index
#         0   1   2   3    4
list1 = ['a','c','d','e','f']
#         -5  -4  -3  -2  -1
print(list1[-5:3:2])
# if we are going from left to right the increment should be positive that is +2 in above case
# if we are going from right to left the increment should be negative


# # for loop
# for i in range(1,11):
#     print(i)

# In[7]:


for i in range(1,11):
    print(i)


# # Nested For Loop

# In[8]:


for i in range(1,11):
    #i = 2
    for j in range(1,5):
        #j = 2
        print(i, j)


# # While Loop¶

# In[10]:


# While Loop
# if <some condition>:
#    print('Some Action')

# while <some condition>:
#    print('Some Action')

i = 0
while i<10:
    print(i)
    i+=1


# # Create Table 
# 

# In[11]:


for n in range(1,11):
    #print(2,"X",n,"=",n*2)
    #print("2 X "+str(n)+"="+str(n*2))
    print(f'2 X {n} = {n*2}')


# # Create table for user input

# In[12]:


#Program to print the tables with the help of nested for loop
user_input = int(input("Enter Number"))

for t in range(1, user_input + 1):
    for n in range(1,11):
        print(f'{t} X {n} = {t*n}')


# # Table with end keyword

# In[13]:


user = int(input("Enter Number"))
for r in range(1,11):
    for t in range(1, user+1):
        print(f'{t}X{r}={r*t}', end='\t')
    print()


# In[ ]:




