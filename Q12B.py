#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q12B", LpMaximize)  


# In[3]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0
X4 = LpVariable("X4", lowBound=0) # Create a variable x1 >= 0


# In[4]:


prob +=2.50*X1 + 3.25*X2 + 3.90*X3 


# In[6]:


prob +=1*X2 >= 150
prob +=-2*X1 - 2*X2 + 1*X3 <= 0
prob +=1*X1 + 1*X2 + 1*X3 - 1*X4 == 0
prob += 1*X1 - 0.3*X4 <= 0 
prob += 10*X1 + 15*X2 + 20*X3 <= 5760 


# In[7]:


prob


# In[8]:


prob.solve()


# In[9]:


value(X1), value(X2), value(X3),value(X4) ,value(prob.objective)  


# In[ ]:




