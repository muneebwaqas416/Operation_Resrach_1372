#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question – 3.2: 

### Decision Variables

X1 = Number of stoves produced weekly 
X2 = Number of washers produced weekly 
X3 = Number of electric dryers produced weekly 
X4 = Number of gas dryers produced weekly 
X5 = Number of refrigerators produced weekly 


### Objective Function
MAX = Z =  110X1 + 90X2 + 75X3 + 80X4 + 130X5 


### Constraints
5.5X1 + 5.2X2 + 5.0X3 + 5.1X4 + 7.5X5 ≤ 4800 (Molding/pressing)
4.5X1 ≤ 1200 (Stove assembly) 
4.5X2 + 4.0X3 + 3.0X4 ≤ 2400 (Washer/dryer assembly)  
9.0X5 ≤ 1200 (Refrigerator assembly) 
4.0X1 + 3.0X2 + 2.5X3 + 2.0X4 + 4.0X5 ≤ 3000 (Packaging) 
All X's ≥ 0 


# In[4]:


#Importing pulp
from pulp import *


# In[5]:


prob = LpProblem("Q2", LpMaximize)  


# In[6]:


#Ddecision Variables
x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Create another variable x2 >= 0
x3 = LpVariable("x3", lowBound=0) # Create another variable x3 >= 0
x4 = LpVariable("x4", lowBound=0) # Create another variable x4 >= 0
x5 = LpVariable("x5", lowBound=0) # Create another variable x5 >= 0


# In[7]:


#Objective Funtion
prob +=110*x1 + 90*x2 + 75*x3 + 80*x4 + 130*x5 


# In[9]:


prob +=5.5*x1 + 5.2*x2 + 5.0*x3 + 5.1*x4 + 7.5*x5 <= 4800 
prob +=4.5*x1 <= 1200 
prob +=4.5*x2 + 4.0*x3 + 3.0*x4 <= 2400   
prob +=9.0*x5 <= 1200 
prob +=4.0*x1 + 3.0*x2 + 2.5*x3 + 2.0*x4 + 4.0*x5 <= 3000  


# In[10]:


prob


# In[11]:


prob.solve()


# In[12]:


print("Status:", LpStatus[prob.status])


# In[13]:


value(x1), value(x2), value(x3),value(x4),value(x5),value(prob.objective)  


# In[ ]:




