#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Decision Varables
X1 = the number in group I contacted by telephone 
X2 = the number in group II contacted by telephone 
X3 = the number in group III contacted by telephone 
X4 = the number in group IV contacted by telephone 
X5 = the number in group I contacted in person 
X6 = the number in group II contacted in person 
X7 = the number in group III contacted in person 
X8 = the number in group IV contacted in person 


# In[ ]:


##OF
MIN 15X1 + 12X2 + 20X3 + 18X4 + 35X5 + 30X6 + 50X7 + 40X8 


# In[ ]:


##Contraints
 X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 = 2000 (Total) 
 X1 + X2 + X5 + X6 ≥ 1000 (W&R) 
 X5 + X6 + X7 + X8 ≥ 500 (In person) 
-.5X1 + .5X5 ≥ 0 (W&R,ip)  
X2 + X4 + X6 + X8 ≤ 800(Small)
  - .25X2 - .25X4+ .75X6 + .75X8 ≤ 0 (Small,ip)
  X1 + X5 ≥ 200 (Min I)  
X2 + X6 ≥ 200 (Min II)
 X3 + X7 ≥ 200 (Min III) 
 X4 + X8 ≥ 200 (Min IV) 
 X1 + X5 ≤ 1000 (Max I)  
X2 + X6 ≤ 1000 (Max II)  
X3 + X7 ≤ 1000 (Max III) 
 X4 + X8 ≤ 1000 (Max IV) 
All X's≥ 0 


# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q9", LpMinimize)  


# In[3]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0
X4 = LpVariable("X4", lowBound=0) # Create a variable x1 >= 0
X5 = LpVariable("X5", lowBound=0) # Create another variable x2 >= 0
X6 = LpVariable("X6", lowBound=0) # Create another variable x3 >= 0x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
X7 = LpVariable("X7", lowBound=0) # Create another variable x2 >= 0
X8 = LpVariable("X8", lowBound=0) # Create another variable x3 >= 0


# In[4]:


prob +=15*X1 + 12*X2 + 20*X3 + 18*X4 + 35*X5 + 30*X6 + 50*X7 + 40*X8 


# In[6]:


prob += 1*X1 + 1*X2 + 1*X3 + 1*X4 + 1*X5 + 1*X6 + 1*X7 + 1*X8 == 2000 
prob +=1*X1 + 1*X2 + 1*X5 + 1*X6 >= 1000
prob +=1*X5 + 1*X6 + 1*X7 + 1*X8 >= 500
prob += -0.5*X1 + 0.5*X5 >= 0
prob +=1*X2 + 1*X4 + 1*X6 + 1*X8 <= 800
prob += -0.25*X2 - 0.25*X4 + 0.75*X6 + 0.75*X8 <= 0
prob += 1*X1 + 1*X5 >= 200 
prob += 1*X2 + 1*X6 >= 200 
prob += 1*X3 + 1*X7 >= 200  
prob += 1*X4 + 1*X8 >= 200  
prob += 1*X1 + 1*X5 <= 1000  
prob += 1*X2 + 1*X6 <= 1000   
prob += 1*X3 + 1*X7 <= 1000  
prob += 1*X4 + 1*X8 <= 1000  


# In[8]:


prob


# In[9]:


prob


# In[10]:


prob.solve()


# In[12]:


value(X1), value(X2), value(X3),value(X4),value(X5),value(X6),value(X7),value(X8) ,value(prob.objective)  


# In[ ]:




