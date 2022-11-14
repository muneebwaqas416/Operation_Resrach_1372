#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Desicion Vriable
X1 = Number of refrigerator/ovens produced 
X2 = Number of French fry makers produced 
X3 = Number of French toast makers produced 


# In[ ]:


##OF
MIN 140X1 + 50X2 + 36X3 


# In[ ]:


##Contraints
100X1 + 35X2 + 27X3 ≥ 2,000,000 (Min Profit) 
 X1 ≥ 5,000 (Min Refrig/oven) 
 X2 ≥ 4,000 (Min French fry maker) 
 X3 ≥ 2,300 (Min French toast maker) 
 X1 ≤ 15,000 (Max Refrig/oven) 
 X2 ≤ 15,000 (Max French fry maker) 
 X3 ≤ 15,000 (Max French toast maker) 


# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q11", LpMinimize)  


# In[3]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0


# In[4]:


prob +=140*X1 + 50*X2 + 36*X3 


# In[5]:


prob +=100*X1 + 35*X2 + 27*X3 >= 2000000
prob +=1*X1>=5000
prob +=  1*X2 >=4000
prob += 1*X3 >=2300
prob += 1*X1 <=15000
prob += 1*X2 <=15000
prob += 1*X3 <=15000


# In[6]:


prob


# In[7]:


prob.solve()


# In[8]:


value(X1), value(X2), value(X3) ,value(prob.objective)  


# In[ ]:




