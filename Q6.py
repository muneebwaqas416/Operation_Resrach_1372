from docplex.mp.model import Model

m = Model(name='Q6')

##Decision Variables
# X1 = number of 8-oz. portions of steak in the diet 
# X2 = number of ounces of cheese in the diet 
# X3 = number of apples in the diet 
# X4 = number of 8-oz. portion of milk in the diet 

##OF
# MIN 51X1 + 9X2 + 1X3 + 8X4 

##Variables
X1 = m.continuous_var(name='X1')
X2 = m.continuous_var(name='X2')
X3 = m.continuous_var(name='X3')
X4 = m.continuous_var(name='X4')

##CONSTRAINTS
m.add_constraint(m.sum([692*X1 , 110*X2 , 81*X3 , 150*X4]) >= 1410)
m.add_constraint(m.sum([692*X1 , 110*X2 , 81*X3 , 150*X4]) <= 1610)
##57X1 + 6X2 + 1X3 + 8X4 ≥ 85
m.add_constraint(m.sum([57*X1 , 6*X2 , 1*X3 , 8*X4 ])>=85)
m.add_constraint(m.sum([1*X2 , 22*X3 , 12*X4  ]) >=25)
##m.add_constraint([X1>=0 , X2>=0 , X3>=0 , X4>=0])

##OBJECTIVE

m.minimize(51*X1 + 9*X2 + 1*X3 + 8*X4 )

sol = m.solve()

sol.display()

















