import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# define energy balance model
def heat(x, t):
    # parameters
    Ta = 23 + 273.15
    U = 10.0
    m = 4.0 / 1000.0
    Cp = 0.5 * 1000.0
    A = 12.0 / 100.0**2
    alpha = 0.01
    eps = 0.9
    sigma = 5.67e-8

    if t>10 and t<=400:
        Q = 100.0
    else:
        Q = 0.0

    # temperature state
    T = x[0]

    dTdt = ((U*A)*(Ta-T) + (eps * sigma * A * (Ta**4 - T**4)) + alpha * Q) / (m * Cp)

    return dTdt

T0 = 23 + 273.15
time = np.linspace(0,600,601)
T = odeint(heat,T0,time) # Integrate ODE

# Plot results
plt.figure(1)
plt.plot(time/60.0,T-273.15,'b-')
plt.ylabel('Temperature (degC)')
plt.xlabel('Time (min)')
plt.legend(['Step Test (0-100% heater)'])
plt.show() 