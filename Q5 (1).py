#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Decision Variable
X1 = Number of full comforters produced daily
X2 = Number of queen comforters produced daily
X3 = Number of king comforters produced daily

#O.F
MAX 6.50X1 + 9.00X2 + 10.00X3

##Contraints
3X1 + 4X2 + 6X3 ≤ 2,700 (Stuffing)
55X1 + 75X2 + 95X3 ≤ 48,000 (Fabric)
3X1 + 5X2 + 6X3 ≤ 3,000 (Cutting minutes)
5X1 + 6X2 + 8X3 ≤ 12,000 (Sewing minutes) 
All X's ≥ 120 


# In[43]:


from pulp import *
import matplotlib.pyplot as plt
import numpy as np


# In[44]:


##Define Problem
prob = LpProblem("Q5",LpMaximize)


# In[45]:


#Decision Variable
x1 = LpVariable("x1", lowBound=120) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=120) # Create another variable x2 >= 0
x3 = LpVariable("x3", lowBound=120) # Create another variable x3 >= 0


# In[46]:


##O.F
prob +=6.50*x1 + 9.00*x2 + 10.00*x3


# In[59]:


#Contraints
prob +=3*x1 + 4*x2 + 6*x3 <= 2700
prob +=55*x1 + 75*x2 + 95*x3 <= 48,000
prob +=3*x1 + 5*x2 + 6*x3 <= 3,000 
prob +=5*x1 + 6*x2 + 8*x3 <= 12,000


# In[60]:


prob


# In[61]:


prob.solve()


# In[62]:


print("Status:", LpStatus[prob.status])


# In[63]:


value(x1), value(x2),value(x3),value(prob.objective)  


# In[52]:


for v in prob.variables():
    print (v.name, "=", v.varValue)


# In[ ]:




