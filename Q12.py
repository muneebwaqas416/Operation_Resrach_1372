#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Decision Variables
X1 = Number of plates made per day 
X2 = Number of mugs made per day 
X3 = Number of steins made per day 
X4 = Total daily production 


# In[ ]:


##OF
MAX 2.50X1 + 3.25X2 + 3.90X3 


# In[ ]:


##Const
 2X1 + 3X2 + 6X3 ≤ 1920 ((4)(8)(60) Molding min.)  
8X1 + 12X2 + 14X3 ≤ 3840 ((8)(8)(60) Finishing min.) 
 X2 ≥ 150 (Minimum mugs)
 -2X1 - 2X2 + X3 ≤ 0 (Steins ≤ 2(Plates + Mugs) 
 X1 + X2 + X3 - X4 = 0 (Total Definition) 
 X1 - .3X4 ≤ 0 (Plates ≤ 30% Total Produced) 


# In[2]:


from pulp import *


# In[3]:


prob = LpProblem("Q12", LpMaximize)  


# In[4]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0
X4 = LpVariable("X4", lowBound=0) # Create a variable x1 >= 0


# In[5]:


prob +=2.50*X1 + 3.25*X2 + 3.90*X3 


# In[6]:


prob +=  2*X1 + 3*X2 + 6*X3 <= 1920
prob +=8*X1 + 12*X2 + 14*X3 <= 3840
prob +=1*X2 >= 150
prob +=-2*X1 - 2*X2 + 1*X3 <= 0
prob +=1*X1 + 1*X2 + 1*X3 - 1*X4 == 0
prob += 1*X1 - 0.3*X4 <= 0 


# In[7]:


prob


# In[8]:


prob.solve()


# In[9]:


value(X1), value(X2), value(X3),value(X4) ,value(prob.objective)  


# In[ ]:




