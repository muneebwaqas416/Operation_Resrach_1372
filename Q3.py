#!/usr/bin/env python
# coding: utf-8

# In[23]:


##Decision Variables
X1 = the number of standard Z345’s produced weekly 
X2 = the number of industrial Z345’s produced weekly 
X3 = the number of standard W250’s produced weekly 
X4 = the number of industrial W250’s produced weekly 
X5 = the total number of products produced weekly 

##OF
MAX 400X1 + 560X2 + 560X3 + 700X4 

##Constraints 
25X1 + 46X2 + 16X3 + 34X4 ≤ 2500 (zinc) 
50X1 + 30X2 + 28X3 + 12X4 ≤ 2800 (iron) 
X1 + X2 ≥ 20 (Min Z345’s) 
X1 + X2 + X3 + X4 - X5 = 0 (X5 definition)  
X2 + X4 - .50X5 ≥ 0 (Industrial min.)  
X1 + X2 - .75X5 ≤ 0 (Max Z345’s) 
X3 + X4 - .75X5 ≤ 0 (Max W250’s) 
X1, X2, X3, X4, X5 ≥ 0


# In[ ]:


#importing from pulp
from pulp import * 


# In[4]:


#Defijne Problem
prob = LpProblem("Q3",LpMaximize)


# In[9]:


#Define D.V
x1 = LpVariable("x1",lowBound=0)
x2 = LpVariable("x2",lowBound=0)
x3 = LpVariable("x3",lowBound=0)
x4 = LpVariable("x4",lowBound=0)
x5 = LpVariable("x5",lowBound=0)


# In[11]:


#O.F
prob +=400*x1+560*x2+560*x3+700*x4+0*x5


# In[16]:


#Constraints
prob +=25*x1 + 46*x2 + 16*x3 + 34*x4 <= 2500  
prob +=50*x1 + 30*x2 + 28*x3 + 12*x4 <= 2800  
prob +=1*x1 + 1*x2 >= 20 
prob +=1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 ==0   
prob +=1*x2 + 1*x4 - 0.50*x5 >= 0   
prob +=1*x1 + 1*x2 - 0.75*x5 <= 0 
prob +=1*x3 + 1*x4 - 0.75*x5 <= 0  


# In[18]:


prob


# In[19]:


prob.solve()


# In[20]:


print("Status:", LpStatus[prob.status])


# In[22]:


value(x1), value(x2), value(x3),value(x4),value(x5),value(prob.objective)


# In[ ]:




