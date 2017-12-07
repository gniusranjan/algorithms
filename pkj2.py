import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def derivN1(y,t):
    yprime=np.array([1-0.7*y[0]])
    return yprime

def derivN2(y,t):
    yprime=np.array([1-0.3*y[0]])
    return yprime

start=0
end=1
numsteps=10
time=np.linspace(start,end,numsteps)
y0=np.array([10])

yN1=integrate.odeint(derivN1,y0,time)
yN2=integrate.odeint(derivN2,y0,time)

print(yN1,'\n',yN2)
plt.plot(time,yN1[:])
plt.plot(time,yN2[:])