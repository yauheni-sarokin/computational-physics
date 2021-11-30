from vpython import *
from numpy import arccos, sqrt

scene.width, scene.height = 900, 900

origin_vactor = vector(0, 0, 0)
# length of rope L
l_rope = 1
# down vector
down_vector = vector(0, -l_rope, 0)
# initial angle theta in radians
theta = pi / 8
# free fall acceleration m/s^2
g = -9.81
# ball mass kg
m = 1
# initial position of the ball
pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)
# force acting on the ball down
f_down = m * g

# axis
curve(pos=[vector(-1, 0, 0), vector(1, 0, 0)], color=color.blue)  # x
curve(pos=[vector(0, 1, 0), vector(0, -1, 0)], color=color.red)  # y

ball_radius = 0.1
# ball without trail
ball = sphere(pos=down_vector, radius=ball_radius, color=color.cyan, make_trail=False)

angle_vector = vector(l_rope * sin(theta), - l_rope * cos(theta), 0)
curve(pos=[origin_vactor, angle_vector], color=color.orange)

rope = curve(origin_vactor, vector(ball.pos.x, ball.pos.y, ball.pos.z))
t = 0

# angular_speed = 0
counter = 0
delta_t = 0.04
while counter < 10000:
    counter += 1
    # rope.clear()

    # ball.pos.y = t
    t += delta_t
    # rope = curve(origin_vactor, vector(ball.pos.x, ball.pos.y, ball.pos.z))

    # calculate forces acting on the ball
    x_force: float = m * g * sin(theta)
    # vector_force = sqrt(x_force * 2 + f_down ^ 2)
    vector_force = sqrt(x_force ** 2 + f_down ** 2)
    acceleration = vector_force / m
    print(f'acceleration {acceleration}')
    distance_traveled = (delta_t ** 2) * acceleration
    # print(f'distance traveled {distance_traveled}')
    # calculate delta theta
    cos_delta_theta = 1 - 1 / 2 * ((distance_traveled ** 2) / (l_rope ** 2))
    # print(f'cos delta theta {cos_delta_theta}')
    # delta theta
    delta_theta = arccos(cos_delta_theta)
    theta -= delta_theta
    # print(f'theta {theta}')
    pos_x, pos_y = l_rope * sin(theta), - l_rope * cos(theta)
    # update ball posiiton
    ball.pos.x = pos_x
    ball.pos.y = pos_y
    # update rope
    rope.append(origin_vactor)
    rope.append(vector(ball.pos.x, ball.pos.y, ball.pos.z))
    sleep(0.03)
