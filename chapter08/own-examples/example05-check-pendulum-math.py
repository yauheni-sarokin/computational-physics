from numpy import arccos, sqrt, pi, sin, cos, array, add, arctan
import functions.canvas as canvas
from vpython import sleep

# Length of rope in meters
l_rope = 1
# squared length of rope
l_rope_squared = l_rope ** 2
# angle theta
theta = (pi / 180) * 50
# gravitational constant m / s ** 2
g = -9.81
# mass of the sphere in kg
m = 1

# force due to sphere mass {x, y}
sphere_mass_vector = array([0, m * g])

time = 0
delta_time = 0.001
speed_vector = array([0, 0])

sphere_position = array([l_rope * sin(theta), - l_rope * cos(theta)])


def calculate_theta_from_position() -> float:
    '''
    calculate theta considering sphere position, so theta is angle between negative y axis and
    ball inclined. Короче на бумажке расписал лучше
    :return: theta current
    '''
    x = sphere_position[0]
    y = sphere_position[1]
    angle = arctan(x / -y)

    return angle


def update_sphere_position():
    '''
    This function consider the rope length and update position satisfying the constant lenght of the rope
    :return:
    '''
    pass


# counter = 0

while True:
    canvas.rope_clear()
    # if counter > 100: break
    # counter += 1
    # 1. calculate reaction force acting on the rope
    rope_reaction_force = cos(theta) * m * g
    # print(rope_reaction_force)
    # print(rope_reaction_force)
    # 2. calculate rope reaction force vector
    rope_force_vector = array([rope_reaction_force * sin(theta), - rope_reaction_force * cos(theta)])
    # print(rope_force_vector)
    # 3. calculate forces acting on the sphere
    force_vector = add(rope_force_vector, sphere_mass_vector)
    # print(force_vector)
    # 4. calculate speed and distance increment // F=ma
    speed_vector_increment = (force_vector / m) * delta_time
    distance_vector_increment = speed_vector_increment * delta_time
    # print(distance_vector_increment)
    # x. update speed
    # calculate traveled distance so that the distance increment + speed * delta time
    # todo: update position considering the length of the rope
    # ------------------------------test
    x_incr = sphere_position[0] + distance_vector_increment[0]
    y_incr = sphere_position[1] + distance_vector_increment[1]
    hipothenusa = sqrt(x_incr ** 2 + y_incr ** 2)
    rope_length_decrement = hipothenusa / l_rope
    # distance_vector_increment[0] = distance_vector_increment[0] / rope_length_decrement
    # distance_vector_increment[1] = distance_vector_increment[1] / rope_length_decrement
    # ------------------------------test
    speed_vector = add(speed_vector, speed_vector_increment)
    sphere_position = add(sphere_position, add(distance_vector_increment, speed_vector * delta_time))
    sphere_position = sphere_position / rope_length_decrement
    # print(speed_vector)

    # calculate new theta, will use it only for forces calculation
    # print(sphere_position)
    # print(sqrt(sphere_position[0] ** 2 + sphere_position[1] ** 2))
    # print(calculate_theta_from_position() / pi * 180)
    # print(theta)
    theta = calculate_theta_from_position()
    canvas.set_sphere_position(sphere_position[0], sphere_position[1])
    canvas.set_rope_position(sphere_position[0], sphere_position[1])
    canvas.set_force_arrow_position_and_axis(sphere_position[0], sphere_position[1], force_vector[0] / 10,
                                             force_vector[1] / 10)
    sleep(0.01)
