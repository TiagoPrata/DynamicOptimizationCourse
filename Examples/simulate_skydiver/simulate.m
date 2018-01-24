clear all; close all; clc
addpath('apm') % load APMonitor.com files

y = apm_solve('skydiver',7); z = y.x; % solve numerically

figure(1)
subplot(2,1,1)
plot(z.time,z.x,'r:','LineWidth',2)
hold on
plot(z.time,z.y,'b--','LineWidth',2)
ylabel('Position (m)')
legend('x','y')

subplot(2,1,2)
plot(z.time,z.vx,'r:','LineWidth',2)
hold on
plot(z.time,z.vy,'b--','LineWidth',2)
plot(z.time,z.v,'k--','LineWidth',2)
xlabel('Time (sec)')
ylabel('Velocity (m/s)')
legend('V_x','V_y','V')

figure(2)
plot(z.x,z.y,'r-','LineWidth',2)
xlabel('Position (x)')
ylabel('Position (y)')
