from apm import *
from scipy.integrate import odeint
import numpy as np

# Method #1 with APMonitor
y1 = apm_solve('collocation',7)

# Method #2 Orthogonal Collocation on Finite Element Equations
y2 = apm_solve('ocofe',1)

# Method #3 with ODEINT
from collocation import *
y3 = odeint(collocation,[0],[0, 0.5, 1])

print('ODEINT solution')
print('x1 = ' + str(y3[1]))
print('x2 = ' + str(y3[2]))
print(' ')
print('States with Orthogonal Collocation')
print('x1 = ' + str(y2['x1']))
print('x2 = ' + str(y2['x2']) + ' (Matrix) vs ' + str(y1['x'][-1]) + ' (APM)')
