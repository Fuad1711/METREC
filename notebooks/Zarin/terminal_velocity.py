import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
g=9.8
m=1
k=0.25
def a(t,Y):
    y,v=Y
    dydt=v
    dvdt=g-(k/m)*v**2
    return[dydt,dvdt]
def ground(t,Y):
    y,v=Y
    return y
ground.terminal=True
ground.direction=-1
t_span=[0,10]
t_eval=np.linspace(0,10,300)
Y0=[100,0]
sol=solve_ivp(fun=a,t_span=t_span,y0=Y0,t_eval=t_eval,events=ground)
plt.plot(sol.t, sol.y[1])
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time (Falling with drag)")
plt.grid()
plt.show()