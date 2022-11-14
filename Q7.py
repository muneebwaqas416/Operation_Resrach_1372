from docplex.mp.model import Model

m = Model(name='Q7')

##D.V
# X1 = Number of Student models produced each week 
# X2 = Number of Plus models produced each week 
# X3 = Number of Net models produced each week 
# X4 = Number of Pro models produced each week 

##O.F
# MAX 70X1 + 80X2 + 130X3 + 150X4 

##Variables
X1 = m.continuous_var(name='X1')
X2 = m.continuous_var(name='X2')
X3 = m.continuous_var(name='X3')
X4 = m.continuous_var(name='X4')

##CONSTRAINTS
# X3 ≥ 100 (Contract) 
# .4X1 + .5X2 + .6X3 + .8X4 ≤ 750 (Production Hours) 
#  X1 + + X3 ≤ 700 (Celeron) 
#  X2 + X4 ≤ 550 (Pentium) 
#  X1 + X2 + X3 + ≤ 800 (20gb Hard Drives) 
#  X4 ≤ 950 (30gb Hard Drives) 
#  X1 + X2 + 2X3 + X4 ≤ 1600 (Floppy Drives) 
#  X1 + X2 + X4 ≤ 1000 (Zip Drives) 
#  X1 + X3 + X4 ≤ 1600 (CD R/W's) 
#  X2 + X3 + X4 ≤ 900 (DVD's) 
#  X1 + X2 ≤ 850 (15-in. monitors) 
#  X3 + X4 ≤ 800 (17-in. monitors) 
#  X2 + X3 ≤ 1250 (Mini-tower cases) 
#  X1 + X4 ≤ 750 (Tower cases) 

m.add_constraint(m.sum([0.4*X1 , 0.5*X2 , 0.6*X3 , 0.8*X4 ]) <=750 )
m.add_constraint(m.sum([1*X1 , 1*X3])<= 700)
##57X1 + 6X2 + 1X3 + 8X4 ≥ 85
m.add_constraint(m.sum([1*X2 , 1*X4]) <= 550)
m.add_constraint(m.sum([1*X1 , 1*X2 , 1*X3]) <= 800)
##m.add_constraint([X1>=0 , X2>=0 , X3>=0 , X4>=0])

m.add_constraint(m.sum([1*X1 , 1*X2 , 2*X3, 1*X4]) <= 1600)
m.add_constraint(m.sum([1*X1 , 1*X2 ,  1*X4]) <= 1000)
m.add_constraint(m.sum([1*X1 , 1*X3 , 1*X4]) <= 1600)
m.add_constraint(m.sum([1*X1 , 1*X2 , 1*X3]) <= 800)
#  X2 + X3 + X4 ≤ 900 (DVD's) 
m.add_constraint(m.sum([1*X2 , 1*X3 , 1*X4]) <= 900)

#  X1 + X2 ≤ 850 (15-in. monitors) 
m.add_constraint(m.sum([1*X1 , 1*X2 ]) <= 850)

#  X3 + X4 ≤ 800 (17-in. monitors) 
m.add_constraint(m.sum([1*X3 , 1*X4 ]) <= 800)

#  X2 + X3 ≤ 1250 (Mini-tower cases) 
m.add_constraint(m.sum([1*X2 , 1*X3 ]) <= 1250)


#  X1 + X4 ≤ 750 (Tower cases) 
m.add_constraint(m.sum([1*X1 , 1*X4 ]) <= 750)


# X3 ≥ 100 (Contract) 
m.add_constraint(1*X3 >=100)

#  X4 ≤ 950 (30gb Hard Drives) 
m.add_constraint(1*X4 <=950)


m.add_constraint(1*X1 >=0)

m.add_constraint(1*X2 >=0)

m.add_constraint(1*X3 >=0)

m.add_constraint(1*X4 >=0)


##OBJECTIVE

m.maximize(70*X1 + 80*X2 + 130*X3 + 150*X4)

sol = m.solve()

sol.display()

















