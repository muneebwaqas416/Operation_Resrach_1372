#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Decision Variable
X1 = amount invested EAL stock 
X2 = amount invested BRU stock 
X3 = amount invested  TAT stock 
X4 = amount invested  long term bonds 
X5 = amount invested  short term bonds 
X6 = amount invested the tax deferred annuity 
X7 = the total amount invested  stocks only 

##O.F
MAX 0.15X1 + 0.12 X2 + 0.09X3 + 0.11X4 + 0.085X5 + 0.06X6 

###Constraints 
X1 + X2 + X3 + X4 + X5 + X6 = 50,000 (Total)
X6 ≥ 10,000 (TDA)  X1 + X2 + X3 - X7 = 0 (Stocks) 
X3 -.25X7 ≥ 0 (Min TAT)  
X4 + X5 - X7 ≥ 0(Bond ≥ stock)  
X3 + X5 + X6 ≤ 12,500 (Low %) 
All X's ≥ 0 


# In[3]:


from pulp import *


# In[4]:


#define Problem
prob = LpProblem("Q4",LpMaximize)


# In[8]:


#Decision Variable
x1 = LpVariable("x1",lowBound=0)
x2 = LpVariable("x2",lowBound=0)
x3 = LpVariable("x3",lowBound=0)
x4 = LpVariable("x4",lowBound=0)
x5 = LpVariable("x5",lowBound=0)
x6 = LpVariable("x6",lowBound=0)
x7 = LpVariable("x7",lowBound=0)


# In[9]:


#O.F
prob +=0.15*x1 + 0.12*x2 + 0.09*x3 + 0.11*x4 + 0.085*x5 + 0.06*x6 +0*x7


# In[10]:


#Constraints
prob +=1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 1*x6 == 50,000 
prob +=1*x6 >= 10,000 
prob +=1*x1 + 1*x2 + 1*x3 - 1*x7 == 0  
prob +=1*x3 -0.25*x7 >= 0   
prob +=1*x4 + 1*x5 - 1*x7 >= 0  
prob +=1*x3 + 1*x5 + 1*x6 <= 12,500  


# In[11]:


prob


# In[12]:


prob.solve()


# In[13]:


print("Status:", LpStatus[prob.status])


# In[14]:


value(x1), value(x2), value(x3),value(x4),value(x5),value(x6),value(x7),value(prob.objective)


# In[ ]:




