### Sequential method with SciPy.integrate.odeint
import numpy as np
from scipy.integrate import odeint

def skydive(z,t):
    # constants
    g = 9.81 # m/s^2, gravitational constant
    m = 80   # kg, mass of skydiver and pack
    if t<61:
        c = 0.2  # N-s^2/m^2, drag coefficient, chute closed
    else:
        c = 10.0 # N-s^2/m^2, drag coefficient, chute open

    # states (z)
    x = z[0]  # meters, horizontal position 
    y = z[1]  # meters, vertical position / elevation
    vx = z[2] # m/s, skydiver horizontal velocity = airplane velocity
    vy = z[3] # m/s, skydiver vertical velocity

    # derived values
    v = np.sqrt(vx**2+vy**2) # m/s, magnitude of velocity
    Fx = -c * vx**2
    Fy = -m*g + c*vy**2

    # calculate derivatives
    dxdt = vx
    dydt = vy
    dvxdt = Fx / m
    dvydt = Fy / m
    dzdt = [dxdt,dydt,dvxdt,dvydt]    

    return dzdt

# initial conditions
z0 = [0,5000,50,0]
# time points
t = np.linspace(0,90,91)
# solve
z1 = odeint(skydive,z0,t)

# parse results
x = z1[:,0]
y = z1[:,1]
vx = z1[:,2]
vy = z1[:,3]
v = np.sqrt(vx**2+vy**2)


### Simultaneous method with APMonitor
# install and load APMonitor
try:
    from apm import *
except:
    import pip
    pip.main(['install','APMonitor'])    
    from apm import *
    
# solve model
z2 = apm_solve('skydiver',7)


### Plot results
import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,x,'r-',linewidth=2)
plt.plot(t,y,'b-',linewidth=2)
plt.plot(z2['time'],z2['x'],'r:',linewidth=3)
plt.plot(z2['time'],z2['y'],'b--',linewidth=3)
plt.ylabel('Position (m)')
plt.legend(['ODEINT x','ODEINT y','APM x','APM y'])

plt.subplot(2,1,2)
plt.plot(t,vx,'r-',linewidth=2)
plt.plot(t,vy,'b-',linewidth=2)
plt.plot(t,v,'k-',linewidth=2)
plt.plot(z2['time'],z2['vx'],'r--',linewidth=3)
plt.plot(z2['time'],z2['vy'],'b--',linewidth=3)
plt.plot(z2['time'],z2['v'],'k--',linewidth=3)
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (m/s)')
plt.legend(['ODEINT V_x','ODEINT V_y','ODEINT V',\
            'APM V_x','APM V_y','APM V'])

plt.figure(2)
plt.plot(z2['x'],z2['y'],'r-')
plt.xlabel('Position (x)')
plt.ylabel('Position (y)')
plt.show()
