from vpython import *

scene.width, scene.height = 700, 700

origin_vector = vector(0, 0, 0)

# axis of plane
curve(pos=[vector(-1, 0, 0), vector(1, 0, 0)], color=color.blue)  # x
curve(pos=[vector(0, 1, 0), vector(0, -1, 0)], color=color.red)  # y

sphere_radius = 0.03

sphere = sphere(pos=origin_vector, radius=sphere_radius, color=color.cyan, make_trail=False)


def set_sphere_position(x, y):
    '''
    set sphere position on x-y plane
    :param x: x position
    :param y: y position
    :return:
    '''
    sphere.pos.x, sphere.pos.y = x, y


rope = curve(origin_vector, origin_vector)


def set_rope_position(x, y):
    rope.append(origin_vector)
    rope.append(vector(x, y, 0))


def rope_clear():
    rope.clear()


# force_arrow = arrow(pos=vector(0, 0, 0), axis=(1, 1, 0), shaftwidth=0.1)
force_arrow = arrow(pos=origin_vector, axis=vector(0 / 10, 0 / 10,
                                                   0), shaftwidth=0.02)


def set_force_arrow_position_and_axis(posx, posy, axisx, axisy):
    force_arrow.pos.x, force_arrow.pos.y = posx, posy
    force_arrow.axis.x, force_arrow.axis.y = axisx, axisy
