import numpy as np
from scipy.integrate import odeint

def reservoir(z,t):
    # constants
    c_1 = 0.03
    c_2 = 0.015
    c_3 = 0.06
    c_4 = 0

    Vuse_1 = 0.03
    Vuse_2 = 0.05
    Vuse_3 = 0.02
    Vuse_4 = 0.00

    evap_c_1 = 1e-5
    evap_c_2 = 1e-5
    evap_c_3 = 1e-5
    evap_c_4 = 0.5e-5

    A_1 = 13.4
    A_2 = 12.0
    A_3 = 384.5
    A_4 = 4400

    if t<=3 and t>=5:
        Vin_1 = 0.21
    else:
        Vin_1 = 0.13
    
    # initial values
    V_1 = z[0]
    V_2 = z[1]
    V_3 = z[2]
    V_4 = z[3]

    h_1 = 1000 * V_1 / A_1
    h_2 = 1000 * V_2 / A_2
    h_3 = 1000 * V_3 / A_3
    h_4 = 1000 * V_4 / A_4

    Vout_1 = c_1 * np.sqrt(h_1)
    Vout_2 = c_2 * np.sqrt(h_2)
    Vout_3 = c_3 * np.sqrt(h_3)
    Vout_4 = c_4 * np.sqrt(h_4)

    Vin_2 = Vout_1
    Vin_3 = Vout_2
    Vin_4 = Vout_3

    Vevap_1 = evap_c_1 * A_1
    Vevap_2 = evap_c_2 * A_2
    Vevap_3 = evap_c_3 * A_3
    Vevap_4 = evap_c_4 * A_4

    # calculate derivatives
    dVdt_1 = Vin_1 - Vout_1 - Vevap_1 - Vuse_1
    dVdt_2 = Vin_2 - Vout_2 - Vevap_2 - Vuse_2
    dVdt_3 = Vin_3 - Vout_3 - Vevap_3 - Vuse_3
    dVdt_4 = Vin_4 - Vout_4 - Vevap_4 - Vuse_4

    dVdt = [dVdt_1, dVdt_2, dVdt_3, dVdt_4]

    return dVdt

A_1 = 13.4
A_2 = 12.0
A_3 = 384.5
A_4 = 4400

c_1 = 0.03
c_2 = 0.015
c_3 = 0.06
c_4 = 0

# initial conditions
z0 = [0.26, 0.18, 0.68, 22.0]
# time points
t = np.linspace(0,12,13)
# solve
z = odeint(reservoir,z0,t)

V_1 = z[:,0]
V_2 = z[:,1]
V_3 = z[:,2]
V_4 = z[:,3]

h_1 = 1000 * V_1 / A_1 
h_2 = 1000 * V_2 / A_2 
h_3 = 1000 * V_3 / A_3 
h_4 = 1000 * V_4/ A_4 

Vin = [0.13,0.13,0.13,0.21,0.21,0.21,0.13,0.13,0.13,0.13,0.13,0.13,0.13]
Vout_1 = c_1 * np.sqrt(h_1)
Vout_2 = c_2 * np.sqrt(h_2)
Vout_3 = c_3 * np.sqrt(h_3)

import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(311)
plt.plot(t,h_1,'r-')
plt.plot(t,h_2,'b--')
plt.ylabel('Level (m)')
plt.legend(['Jordanelle Reservoir','Deer Creek Reservoir'])

plt.subplot(312)
plt.plot(t,h_3,'g-')
plt.plot(t,h_4,'k:')
plt.ylabel('Level (m)')
plt.legend(['Great Salt Lake','Utah Lake'])

plt.subplot(313)
plt.plot(t,Vin,'k-')
plt.plot(t,Vout_1,'r-')
plt.plot(t,Vout_2,'b--')
plt.plot(t,Vout_3,'g-')
plt.xlabel('Time (month)')
plt.ylabel('Flow (km3/yr)')
plt.legend(['Supply Flow','Upper Provo River','Lower Provo River','Jordan River'])

plt.show()
