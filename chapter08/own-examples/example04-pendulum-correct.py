from vpython import *
from numpy import arccos, sqrt, pi, sin, cos, array, add, arctan

scene.width, scene.height = 700, 700

origin_vector = vector(0, 0, 0)

# Length of rope in meters
l_rope = 1
# squared length of rope
l_rope_squared = l_rope ** 2
# angle theta
theta = (pi / 180) * 40
# gravitational constant m / s ** 2
g = -9.81
# mass of the sphere in kg
m = 1

# initial position of the sphere
pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)
x_force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(0, 0, 0), shaftwidth=0.02)
y_force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(0, 0, 0), shaftwidth=0.02)

# axis of plane
curve(pos=[vector(-1, 0, 0), vector(1, 0, 0)], color=color.blue)  # x
curve(pos=[vector(0, 1, 0), vector(0, -1, 0)], color=color.red)  # y

ball_position_vector = vector(pos_x, pos_y, 0)
ball_radius = 0.1
# ball without trail
ball = sphere(pos=ball_position_vector, radius=ball_radius, color=color.cyan, make_trail=False)
# rope
rope = curve(origin_vector, ball_position_vector)

# force due to sphere mass {x, y}
sphere_mass_vector = array([0, m * g])
# rope reaction force
# rope_reaction_force = cos(theta) * m * g
# rope reaction force vector {x, y}
# rope_force_vector = array([rope_reaction_force * sin(theta), - rope_reaction_force * cos(theta)])
# print(rope_force_vector)
# total_force_vector = add(sphere_mass_vector, rope_force_vector)
# print(total_force_vector)

# force_vector = array([0, 0])

time = 0
delta_time = 0.01
counter = 0

# vector incuding previous forces
# force_vector = array([0, 0])
# force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(force_vector[0] / 10, force_vector[1] / 10,
#                                                              0), shaftwidth=0.1)
force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(0 / 10, 0 / 10,
                                                             0), shaftwidth=0.1)
# force_arrow = arrow(pos=vector(pos_x, pos_y, 0), axis=vector(force_vector[0], force_vector[1], 0))

speed_vector = array([0, 0])

while True:
    # print('cycle')
    rope.clear()
    # all the additionally forces acting on the ball at this moment
    # start from calculation iof the forces acting on the rope
    rope_reaction_force = cos(theta) * m * g
    # rope reaction force vector {x, y}
    rope_force_vector = array([rope_reaction_force * sin(theta), - rope_reaction_force * cos(theta)])
    # total force vector acting on the ball
    total_force_vector = add(rope_force_vector, sphere_mass_vector)

    # force_vector = add(force_vector, total_force_vector)
    # print(f'force vector {force_vector} theta {theta * 180 / pi}')

    # calculate distance traveled, newtons law F = ma, a = F/m, l = F/m * dt**2
    vector_distance_increment = (total_force_vector / m) * (delta_time ** 2)
    vector_speed_increment = (total_force_vector / m) * delta_time
    # теперь либо увеличить скорость после сдвига либо до
    speed_vector = add(speed_vector, vector_speed_increment)

    distance_vector = add(vector_distance_increment, speed_vector * delta_time)

    # vector_distance = add(vector_distance, speed_vector * delta_time)

    # speed_vector_increment = vector_distance_increment / delta_time
    # speed_vector = add(speed_vector, speed_vector_increment)
    # print(f'speed increment {speed_vector}')

    # distance_traveled = sqrt(vector_distance_increment[0] ** 2 + vector_distance_increment[1] ** 2)
    distance_traveled = sqrt(distance_vector[0] ** 2 + distance_vector[1] ** 2)
    # cos of delta theta
    cos_delta_theta = 1 - (1 / 2) * ((distance_traveled ** 2) / l_rope_squared)
    # delta theta
    # todo: Error is here, the delta force continue adding, calculate it some how from the vectors

    # strange weird construction becouse I dont know triginometry
    multiplier = 1
    if speed_vector[0] < 0:
        multiplier = 1
    elif speed_vector[0] > 0:
        multiplier = -1

    delta_theta = arccos(cos_delta_theta) * multiplier
    theta -= delta_theta
    # new position of the sphere
    pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)

    force_arrow.pos.x = pos_x
    force_arrow.pos.y = pos_y
    force_arrow.axis.x = total_force_vector[0] / 10
    force_arrow.axis.y = total_force_vector[1] / 10
    # update ball posiiton
    ball.pos.x = pos_x
    ball.pos.y = pos_y
    # update rope
    rope.append(origin_vector)
    rope.append(vector(pos_x, pos_y, 0))

    counter += 1
    time += delta_time
    sleep(0.1)
