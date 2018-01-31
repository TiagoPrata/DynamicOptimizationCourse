clear all; close all; clc
addpath('apm')

% Method #1 with APMonitor
y1 = apm_solve('collocation',7);
z1 = y1.x;

% Method #2 Orthogonal Collocation on Finite Element Equations
y2 = apm_solve('ocofe',1);
z2 = y2.x;

% Method #3 with ODE15s
[t,z3] = ode15s('collocation',[0 0.5 1], [0]);

disp('ODE15s (MATLAB) solution')
disp(['x1 = ' num2str(z3(2,1))])
disp(['x2 = ' num2str(z3(3,1))])
disp(' ')
disp('States with Orthogonal Collocation')
disp(['x1 = ' num2str(z2.x1)])
disp(['x2 = ' num2str(z2.x2) ' (Matrix) vs ' num2str(z1.x(end)) ' (APM)'])
