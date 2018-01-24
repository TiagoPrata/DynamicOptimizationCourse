# simulate reservoirs
from apm import *
y = apm_solve('reservoirs',7);

# convert time to months from years
time = [x * 12 for x in y['time']] 

# plot results
import matplotlib.pyplot as plt
plt.figure(1)

plt.subplot(311)
plt.plot(time,y['h[1]'],'r-')
plt.plot(time,y['h[2]'],'b--')
plt.ylabel('Level (m)')
plt.legend(['Jordanelle Reservoir','Deer Creek Reservoir'])

plt.subplot(312)
plt.plot(time,y['h[4]'],'g-')
plt.plot(time,y['h[3]'],'k:')
plt.ylabel('Level (m)')
plt.legend(['Great Salt Lake','Utah Lake'])

plt.subplot(313)
plt.plot(time,y['vin[1]'],'k-')
plt.plot(time,y['vout[1]'],'r-')
plt.plot(time,y['vout[2]'],'b--')
plt.plot(time,y['vout[3]'],'g-')
plt.xlabel('Time (month)')
plt.ylabel('Flow (km3/yr)')
plt.legend(['Supply Flow','Upper Provo River','Lower Provo River','Jordan River'])
plt.show()
