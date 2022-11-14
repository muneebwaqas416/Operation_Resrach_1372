#!/usr/bin/env python
# coding: utf-8

# In[5]:


##Decision Varialbes
X1 = the number of Delta assemblies produced daily 
X2 = the number of Omega assemblies produced daily 
X3 = the number of Theta assemblies produced daily 


# In[ ]:


##OBjective Funtion
MAX = Z= 800X1 + 900X2 + 600X3 


# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q8", LpMaximize)  


# In[3]:


x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Create another variable x2 >= 0
x3 = LpVariable("x3", lowBound=0) # Create another variable x3 >= 0


# In[6]:


prob +=800*x1 + 900*x2 + 600*x3 


# In[7]:



prob += 1*x1 + 1*x2 + 1*x3 <= 7  
prob +=2*x1 + 1*x2 +1*x3 <=8 
prob +=80*x1 + 160*x2 + 80*x3  <= 480


# In[8]:


prob


# In[9]:


prob.solve()


# In[10]:


value(x1), value(x2), value(x3),  value(prob.objective)  


# In[ ]:




