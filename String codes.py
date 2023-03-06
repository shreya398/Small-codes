#!/usr/bin/env python
# coding: utf-8

# In[1]:


name="Shreya Subhash Guggare"


# In[2]:


#Capitalize - makes first character of String Capital and rest all lower
name.capitalize()


# In[14]:


" ".join(name)


# In[15]:


#Reversed - reverses a string
reversed(name)


# In[16]:


# use .join to display reversed string
" ".join(reversed(name))


# In[17]:


list(reversed(name))


# In[19]:


name.split(" ")


# In[21]:


name.split(" ")[::-1]


# In[32]:


name.split(" ")[::-1][1]


# In[23]:


name.split(" ")[::-1][2]


# In[24]:


" * ".join(name)


# In[25]:


#Return a copy of the string with leading and trailing whitespace removed.
name.strip()


# In[26]:


a = 'jandmnflkdrg    '


# In[27]:


a.strip()


# In[28]:


a


# In[29]:


b= "Good Morning Dharwad"


# In[30]:


b.replace('Dharwad','Sankeshwar')


# In[31]:


b.replace("oo","  ")


# In[33]:


name


# In[34]:


name.islower()


# In[35]:


name.isupper()


# In[36]:


"".isspace()


# In[37]:


" ".isspace()


# In[38]:


name.endswith("e")


# In[39]:


name.endswith("t")


# In[40]:


name.split(" ")[1].endswith("h")


# In[41]:


x= "jndf745732d"


# In[42]:


x.isalnum()


# In[ ]:


#Reversing the string


# In[43]:


n="Shreya"


# In[45]:


l=len(n)-1
while l!=-1:
    print(n[l])
    l=l-1


# In[46]:


l=len(n)-1
while l!=-1:
    print(n[l],end=(""))
    l=l-1


# In[47]:


n[::-1]


# In[ ]:


#spliting the name into different columns


# In[4]:


import pandas as pd


# In[5]:


df= pd.DataFrame({"fullname":["Shreya Subhash Guggare"]})


# In[6]:


df


# In[56]:


df.values[0][0]


# In[57]:


df.values[0][0].split(" ")


# In[60]:


df.fullname.array[0].spilt(" ")


# In[61]:


df.fullname.dtypes


# In[62]:


#converting object dtype into string
df.fullname.str


# In[63]:


type(df.fullname.str)


# In[64]:


df.fullname.dtypes


# In[65]:


df.fullname.str.split(" ")


# In[7]:


df.fullname.str.split(" ",expand=True)


# In[8]:


df[["first_name","middle_name","last_name"]]=df.fullname.str.split(" ",expand=True)
df


# In[9]:


#Printing the all the vowels in the string


# In[13]:


name="Shreya Subhash Guggare"
vowels="AEIOUaeiou"
for i in name:
    if i in vowels:
        print (i,end=(" "))


# In[14]:


def vowels(string):
    vowels="AEIOUaeiou"
    for i in string:
        if i in vowels:
            print(i,end=" ")


# In[15]:


vowels("LOVE YOU")


# In[ ]:




