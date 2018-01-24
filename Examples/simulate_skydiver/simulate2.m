clear all; close all; clc

%% Method 1: MATLAB integration with ode15s
% initial conditions
z0 = [0,5000,50,0];
% time points
t = linspace(0,90,1);
% solve
[t,z1] = ode15s('skydiver',t,z0);

% parse results
ode_x = z1(:,1);
ode_y = z1(:,2);
ode_vx = z1(:,3);
ode_vy = z1(:,4);
ode_v = sqrt(ode_vx.^2+ode_vy.^2);


%% Method 2: APMonitor
addpath('apm') % load APMonitor.com files
y = apm_solve('skydiver',7); z = y.x; % solve numerically


%% Plot results
figure(1)
subplot(2,1,1)
plot(t,ode_x,'r-','LineWidth',2)
hold on
plot(t,ode_y,'b-','LineWidth',2)
plot(z.time,z.x,'r:','LineWidth',3)
plot(z.time,z.y,'b--','LineWidth',3)
ylabel('Position (m)')
legend('x','y')

subplot(2,1,2)
plot(t,ode_vx,'r-','LineWidth',2)
hold on
plot(t,ode_vy,'b-','LineWidth',2)
plot(t,ode_v,'k-','LineWidth',2)
plot(z.time,z.vx,'r:','LineWidth',3)
plot(z.time,z.vy,'b--','LineWidth',3)
plot(z.time,z.v,'k--','LineWidth',3)
xlabel('Time (sec)')
ylabel('Velocity (m/s)')
legend('V_x','V_y','V','APM V_x','APM V_y','APM V')

figure(2)
plot(z.x,z.y,'r-','LineWidth',2)
xlabel('Position (x)')
ylabel('Position (y)')
