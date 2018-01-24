%% clear session
clear all; close all; clc

%% simulate reservoirs
addpath('apm')
y = apm_solve('reservoirs',7);
z = y.x;

% convert time to months from years
time = round(z.time * 12);

%% plot results
figure(1)

subplot(3,1,1)
plot(time,z.h1,'r-','LineWidth',2)
hold on
plot(time,z.h2,'b--','LineWidth',2)
ylabel('Level (m)')
legend('Jordanelle Reservoir','Deer Creek Reservoir')

subplot(3,1,2)
plot(time,z.h4,'g-','LineWidth',2)
hold on
plot(time,z.h3,'k:','LineWidth',2)
ylabel('Level (m)')
legend('Great Salt Lake','Utah Lake')

subplot(3,1,3)
plot(time,z.vin1,'k-','LineWidth',2)
hold on
plot(time,z.vout1,'r-','LineWidth',2)
plot(time,z.vout2,'b--','LineWidth',2)
plot(time,z.vout3,'g-','LineWidth',2)
xlabel('Time (month)')
ylabel('Flow (km^3/yr)')
legend('Supply Flow','Upper Provo River','Lower Provo River','Jordan River')