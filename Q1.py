#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question – 3.1: 

### Decision Variables

X1 = Number of 20-inch girls bicycles produced this week 
X2 = Number of 20-inch boys bicycles produced this week 
X3 = Number of 26-inch girls bicycles produced this week 
X4 = Number of 26-inch boys bicycles produced this week 


### Objective Function
MAX= Z =  27X1 + 32X2 + 38X3 + 51X4 

### Constraints
X1 + X3 ≥ 200 (Min girls models) 
X2 + X4 ≥ 200 (Min boys models) 
12X1 + 12X2 + 9X3 + 9X4 ≤ 4800 (Production minutes) 
6X1 + 9X2 + 12X3 + 18X4 ≤ 4800 (Assembly minutes) 
2X1 + 2X2 ≤ 500 (20-inch tires) 
2X3 + 2X4 ≤ 800 (26-inch tires) 
All X's ≥ 0 


# In[7]:


#Importing pulp
from pulp import *


# In[8]:


prob = LpProblem("Q1", LpMaximize)  


# In[14]:


#Ddecision Variables
x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Create another variable x2 >= 0
x3 = LpVariable("x3", lowBound=0) # Create another variable x3 >= 0
x4 = LpVariable("x4", lowBound=0) # Create another variable x4 >= 0


# In[17]:


#Objective Funtion
prob +=27*x1+32*x2+38*x3+51*x4


# In[19]:


#Constraints 
prob += 1*x1 + 1*x3 >= 200  
prob +=1*x2 + 1*x4 >= 200 
prob +=12*x1 + 12*x2 + 9*x3 + 9*x4 <= 4800  
prob +=6*x1 + 9*x2 + 12*x3 + 18*x4 <= 4800  
prob +=2*x1 + 2*x2 <= 500  
prob +=2*x3 + 2*x4 <= 800 


# In[20]:


prob


# In[21]:


prob.solve()


# In[22]:


print("Status:", LpStatus[prob.status])


# In[23]:


value(x1), value(x2), value(prob.objective)  


# In[ ]:




