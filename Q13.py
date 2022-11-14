#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##DV
X1 = $ invested in first trust deeds 
X2 = $ invested in second trust deeds 
X3 = $ invested in third trust deeds 
X4 = $ invested in commercial trust deeds 
X5 = $ invested in a savings account 
X6 = Total $ invested in residential trust deeds 
X7 = Total $ invested in all trust deeds 


# In[ ]:


##OF
MAX .0775X1 +.1125X2 +.1425X3 +.9875X4 +.0445X5


# In[ ]:


X1 + X2 + X3 + X4 + X5 = 68,000,000 (Total)  
 X5 ≥ 5,000,000 (Save) 
 X1 + X2 + X3 + - X6 = 0 (Res Tr.) 
 X1 + X2 + X3 + X4 -X7 = 0 (Total Tr) 
 X6 - .8X7 ≥ 0 (80% Res.) 
 X1 -.6X6 ≥ 0 (60% First)  
4X1 + 6X2 + 9X3 + 3X4 ≤340,000,000 (*)
 All X's ≥ 0 


# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q13", LpMaximize)  


# In[3]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0
X4 = LpVariable("X4", lowBound=0) # Create a variable x1 >= 0
X5 = LpVariable("X5", lowBound=0) # Create another variable x2 >= 0
X6 = LpVariable("X6", lowBound=0) # Create another variable x3 >= 0x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
X7 = LpVariable("X7", lowBound=0) # Create another variable x2 >= 0


# In[4]:


prob +=0.0775*X1 +0.1125*X2 + 0.1425*X3 + 0.9875*X4 + 0.0445*X5


# In[6]:


prob += 1*X1 + 1*X2 + 1*X3 + 1*X4 + 1*X5 == 68000000
prob +=1*X5 >= 5000000
prob +=1*X1 + 1*X2 + 1*X3 + - 1*X6 == 0
prob += 1*X1 + 1*X2 + 1*X3 + 1*X4 -1*X7 == 0
prob +=1*X6 - 0.8*X7 >= 0
prob +=1*X1 -0.6*X6 >= 0
prob += 4*X1 + 6*X2 + 9*X3 + 3*X4 <= 340000000


# In[7]:


prob


# In[8]:


prob.solve()


# In[9]:


value(X1), value(X2), value(X3),value(X4),value(X5),value(X6),value(X7),value(prob.objective)  


# In[ ]:




