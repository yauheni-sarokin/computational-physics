from numpy import arccos, sqrt, pi, sin, cos

l_rope = 1
l_rope_squared = l_rope ** 2
theta = pi / 8
g = -9.81  # m/s^2
m = 1  # m

pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)
print(f'x {pos_x}, y {pos_y}')

time = 0
delta_time = 0.1

counter = 0
# acceleration = 0
# x_acceleration, y_acceleration = 0, 0
# x_force = 0
while counter < 150:
    # acceleration of ball
    theta_acceleration = (g / l_rope) * sin(theta * time)

    delta_theta = theta_acceleration * (delta_time ** 2)
    theta += delta_theta
    print(theta)

    time += delta_time
    counter += 1
