clear all; close all; clc
addpath('apm') % load APM Toolbox

% define server and application names
s = 'http://byu.apmonitor.com';
a = 'node_test';

sol = []; % store solution
for nodes = 2:6,
    apm(s,a,'clear all'); % clear prior application
    apm_load(s,a,'collocation.apm'); % load model
    csv_load(s,a,'collocation.csv'); % load data
    apm_option(s,a,'nlc.imode',4);   % imode = 4, simulation
    apm_option(s,a,'nlc.nodes',nodes); % nodes (2-6)
    apm(s,a,'solve'); % solve problem
    y = apm_sol(s,a); z = y.x; % retrieve solution
    sol = [sol z.x(end)];
end

disp(sol)