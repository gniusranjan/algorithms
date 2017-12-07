

### Code for CANCER METASTASIS
# sample values of constants
## alpha , healthy cells = 0.1
## alpha , cancerous cells = 0.45
## beta , healty cell = 0.11
## beta , cancerous cells = 0.15
## dosage values of drugs = 0.65 - 1.0


from numpy import *
from scipy import integrate
import pylab as p
a = float(input('the value of alpha for healthy cells : '))
b = float(input('the value of beta for healthy cells : '))
A = float(input('the value of alpha for cancerous cells : '))
B = float(input('the value of beta for cancerous cells : '))
hi = float(input('initial concentration of healthy cells : '))
ci = float(input('intial concentration of cancerous cells : '))
d = float(input('dosage for the cells : '))

time= float(input('the duration of time interval for which you want to examine : '))

## SOLVING THE DIFFERENTIAL EQUATION

def dX_dt(X, t=0):
    """ Return the growth rate of healthy and cancerous cells. """
    return array([ a*X[0] - b*X[0]*X[1]- d*(X[0]**2) ,
                  A*X[1] - B*X[0]*X[1] -d*(X[1]**2) ])

t = linspace(0, time,  10)              # time
X0 = array([hi,ci])                     # initials conditions: 10 healthy and 5 cancerous cells
X = integrate.odeint(dX_dt, X0, t)
print('the integral solution for assumed differential equation')

#equilibrium points
#!python
X_f0 = array([     0. ,  0.])
X_f1 = array([ A/B, a/b])
all(dX_dt(X_f0) == zeros(2) ) and all(dX_dt(X_f1) == zeros(2))

print (X)

#   """ Ploting of graph """
#!python
cancerous_cells, healthy_cells = X.T
f1 = p.figure()
p.plot(t, healthy_cells, 'r-', label='Healthy cells')
p.plot(t, cancerous_cells  , 'b-', label='Cancerous cells')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('change in no of cells')
p.title('Evolution of cancerous and healthy cells')
f1.savefig('cells.png')
p.show()

#!python
def d2X_dt2(X, t=0):
    """ Return the Jacobian matrix evaluated in X. """
    return array([[a -b*X[1]-2*a*X[0],   -b*X[0]     ],
                  [A - B * X[0] - 2 * A * X[1], -B* X[1]]])

## the above method is used to check whether the equilibrium points are saddle points or not.