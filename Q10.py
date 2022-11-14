#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Desicion Variables
X1 = the number of ounces of Multigrain Cheerios in the mixture 
X2 = the number of ounces of Grape Nuts in the mixture 
X3 = the number of ounces of Product 19 in the mixture 
X4 = the number of ounces of Frosted Bran in the mixture 
X5 = the total number of ounces in the mixture 


# In[ ]:


##OF
MIN 12X1 + 9X2 + 9X3 + 15X4 


# In[ ]:


##Constraints
30X1 + 30X2 + 20X3 + 20X4 ≥ 50 (Vitamin A) 
25X1 + 2X2 + 100X3 + 25X4 ≥ 50 (Vitamin C) 
25X1 + 25X2 + 25X3 + 25X4 ≥ 50 (Vitamin D) 
25X1 + 25X2 + 100X3 + 25X4 ≥ 50 (Vitamin B6) 
45X1 + 45X2 + 100X3 + 25X4 ≥ 50 (Iron) 
 X1 + X2 + X3 + X4 - X5 = 0 (Total) 
 X1 - .1X5 ≥ 0 (≥ 10% M/G Cheerios) 
 X2 - .1X5 ≥ 0 (≥ 10% Grape Nuts) 
 X3 - .1X5 ≥ 0 (≥ 10% Product 19) 
 X4 - .1X5 ≥ 0 (≥ 10% Frosted Bran) 


# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Q10", LpMinimize)  


# In[3]:


X1 = LpVariable("X1", lowBound=0) # Create a variable x1 >= 0
X2 = LpVariable("X2", lowBound=0) # Create another variable x2 >= 0
X3 = LpVariable("X3", lowBound=0) # Create another variable x3 >= 0
X4 = LpVariable("X4", lowBound=0) # Create a variable x1 >= 0
X5 = LpVariable("X5", lowBound=0) # Create another variable x2 >= 0


# In[4]:


prob +=12*X1 + 9*X2 + 9*X3 + 15*X4 


# In[5]:


prob += 30*X1 + 30*X2 + 20*X3 + 20*X4 >= 50
prob +=25*X1 + 2*X2 + 100*X3 + 25*X4 >= 50
prob +=25*X1 + 25*X2 + 25*X3 + 25*X4 >= 50 
prob +=25*X1 + 25*X2 + 100*X3 + 25*X4 >= 50
prob +=45*X1 + 45*X2 + 100*X3 + 25*X4 >= 50
prob += 1*X1 + 1*X2 + 1*X3 + 1*X4 - 1*X5 == 0
prob += 1*X1 - 0.1*X5 >= 0  
prob += 1*X2 - 0.1*X5 >= 0 
prob += 1*X3 - 0.1*X5 >= 0  
prob += 1*X4 - 0.1*X5 >= 0  


# In[6]:


prob


# In[7]:


prob.solve()


# In[8]:


value(X1), value(X2), value(X3),value(X4),value(X5) ,value(prob.objective)  


# In[ ]:




