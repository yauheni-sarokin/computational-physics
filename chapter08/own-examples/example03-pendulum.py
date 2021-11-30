from numpy import arccos, sqrt, pi, sin, cos
from vpython import *

scene.width, scene.height = 900, 900
origin_vector = vector(0, 0, 0)

l_rope = 1
l_rope_squared = l_rope ** 2
# theta = pi / 4
theta = (pi / 180) * (85)
g = -9.81  # m/s^2
m = 1  # m

pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)
x_force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(0, 0, 0), shaftwidth=0.02)
y_force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(0, 0, 0), shaftwidth=0.02)
# down vector
position_vector = vector(pos_x, pos_y, 0)

time = 0
delta_time = 0.01

# axis
curve(pos=[vector(-1, 0, 0), vector(1, 0, 0)], color=color.blue)  # x
curve(pos=[vector(0, 1, 0), vector(0, -1, 0)], color=color.red)  # y

ball_radius = 0.1
# ball without trail
ball = sphere(pos=position_vector, radius=ball_radius, color=color.cyan, make_trail=False)
# rope
rope = curve(origin_vector, position_vector)

counter = 0
# speed_x, speed_y = 0, 0

force_vector_x, force_vector_y = 0, 0

# while counter < 150:
while True:
    rope.clear()
    # find all the forces acting on the ball
    gravity_force = m * g
    rope_force = gravity_force * cos(theta)

    # find the orthogonal vector forces, so force components in x and y planes
    # total_force_vector = sqrt(gravity_force ** 2 + rope_force ** 2)
    force_vector_x -= rope_force * sin(theta)
    force_vector_y = rope_force * cos(theta)

    speed_x = (force_vector_x / m) * delta_time
    speed_y = (force_vector_y / m) * delta_time

    # distance traveled
    distance_x = speed_x * delta_time
    distance_y = speed_y * delta_time
    # total distance
    total_distance = sqrt(distance_x ** 2 + distance_y ** 2)
    speed = total_distance / delta_time
    # cos of delta theta
    cos_delta_theta = 1 - (1 / 2) * ((total_distance ** 2) / l_rope_squared)
    # delta theta
    delta_theta = arccos(cos_delta_theta)
    # change of theta angle
    if force_vector_x < 0: delta_theta = delta_theta * -1
    theta -= delta_theta
    # new position
    pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)

    # print(f'x force {force_vector_x:.3f} y force {force_vector_y:.3f} roper force {rope_force:.3f} theta {theta:.3f} speed x {speed_x:.3f} speed y {speed_y:.3f} distance x {distance_x:.3e} distance y {distance_y:.3e} total distance {total_distance:.3e} speed {speed:.3f} theta {theta:.3e} delta theta {delta_theta:.3e} pos x {pos_x:.3e} pos y {pos_y:.3e}')
    # print(f' theta {theta}')

    # update ball posiiton
    ball.pos.x = pos_x
    ball.pos.y = pos_y
    # update rope
    rope.append(origin_vector)
    rope.append(vector(pos_x, pos_y, 0))
    # force arrows
    x_force_arrow.pos = vector(pos_x, pos_y, 0)
    x_force_arrow.axis = vector(vector(force_vector_x / 250, 0, 0))
    y_force_arrow.pos = vector(pos_x, pos_y, 0)
    y_force_arrow.axis = vector(vector(0, force_vector_y / 10, 0))

    time += delta_time
    # counter += 1
    sleep(0.03)
