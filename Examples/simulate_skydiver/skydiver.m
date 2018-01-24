function dzdt = skydiver(t,z)
% constants
g = 9.81; % m/s^2, gravitational constant
m = 80;   % kg, mass of skydiver and pack
if t<61
    c = 0.2;  % N-s^2/m^2, drag coefficient, chute closed
else
    c = 10.0; % N-s^2/m^2, drag coefficient, chute open
end

% states (z)
x = z(1);  % meters, horizontal position
y = z(2);  % meters, vertical position / elevation
vx = z(3); % m/s, skydiver horizontal velocity = airplane velocity
vy = z(4); % m/s, skydiver vertical velocity

% derived values
v = sqrt(vx^2+vy^2); % m/s, magnitude of velocity
Fx = -c * vx^2;
Fy = -m*g + c*vy^2;

% calculate derivatives
dxdt = vx;
dydt = vy;
dvxdt = Fx / m;
dvydt = Fy / m;
dzdt = [dxdt,dydt,dvxdt,dvydt]';

end
