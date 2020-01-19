#!/usr/bin/env python
# coding: utf-8

# In[2]:


personData = {
    "name" : "Ali",
    "age" : 50
}
hobbies = ["reading", "travelling"]
personData["hobbies"] = hobbies
personData


# In[3]:


personData.update({
    "hobbies" : hobbies
})


# In[4]:


personData


# In[5]:


workExp = {
    "title" : "web developer",
    "startDate" : 2015,
    "endDate" : 2019
}
personData.update({
    "experience" : workExp
})


# In[6]:


personData


# In[7]:


personData.get("name")


# In[16]:




personData.get("name")


# In[18]:


personData.update({
    "experience" : workExp
})


# In[19]:


personData


# In[20]:


personData["experience"]


# In[21]:


personData["experience"]["title"]


# In[23]:


a = 6
b = 6
id(a)


# In[24]:


a is b


# In[25]:


list1 = ['Ali', 'Kamran', 'Rashid']
list2 = list1
print(list1)
print(list2)


# In[26]:


list2.append("Zahid")
list2


# In[27]:


list1


# In[28]:


id(list1)


# In[29]:



id(list2)


# In[30]:


list3 = list2.copy()
list3.pop()
list3


# In[31]:


list2 is list1


# In[32]:


list3 is list2


# In[33]:


list4 = [24, "Nadeem", "Kareem", "abc@gmail.com", 34]


# In[34]:


myDict1 = {}


# In[35]:


myDict = {
    "id":24,
    "fName":"Kareem",
    "lName":"Usman",
    "email":"abc@gmail.com",
    "age": 35
}


# In[36]:


myDict1


# In[37]:


myDict


# In[38]:


myDict.keys()


# In[39]:


myDict.values()


# In[40]:


myDict["id"]


# In[41]:


print(myDict.get("fname"))


# In[43]:


myDict.get("ahttp://localhost:8888/notebooks/Untitled2.ipynb?kernel_name=python3#bc","Key not Found")


# In[44]:


myDict2 = myDict.copy()
myDict2


# In[45]:


myDict2["fName"]="Nasir"
myDict2["lName"]="Hussain"
myDict2


# In[46]:


myDict


# In[47]:


myDict2["skills"]=['python','Java','C++']
myDict2


# In[48]:


list5 = ['id','name','fatherName','mobile','email']
myDict7 = dict.fromkeys(list5)
myDict7


# In[49]:


list6=[25,'Ali','Hussain','0345-8765432','xyz@hotmail.com']
print(list5)
print(list6)


# In[50]:


myDict11=dict(zip(list5,list6))
myDict11


# # list of Dictionaries 

# In[58]:


lst=[]
chk=''
while chk.lower() != 'x':
    dict1 = {
        'id': input("Please enter ID: "),
        'name': input("Kindly enter Name: "),
        
        'hobbies': input("Please enter , seperated hobbies: ").split(",") # book reading
    }
    lst.append(dict1)
    chk = input("Enter x to exit and any other key to Continue: ")
lst


# In[ ]:





# In[ ]:




