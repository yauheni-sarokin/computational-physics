from vpython import *

scene.width, scene.height = 900, 900

origin_vactor = vector(0, 0, 0)
# length of rope L
l_rope = 1
# down vector
down_vector = vector(0, -l_rope, 0)
# initial angle theta in radians
theta = 1

# axis
x_axis = curve(pos=[vector(-1, 0, 0), vector(1, 0, 0)], color=color.blue)
x_axis = curve(pos=[vector(0, 1, 0), vector(0, -1, 0)], color=color.red)

ball_radius = 0.1
# ball without trail
ball = sphere(pos=down_vector, radius=ball_radius, color=color.cyan, make_trail=False)

rope = curve(origin_vactor, vector(ball.pos.x, ball.pos.y, ball.pos.z))
t = 0
while True:
    rope.clear()
    ball.pos.x = cos(t)
    ball.pos.y = sin(t)
    # ball.pos.y = t
    t += 0.04
    # rope = curve(origin_vactor, vector(ball.pos.x, ball.pos.y, ball.pos.z))
    rope.append(origin_vactor)
    rope.append(vector(ball.pos.x, ball.pos.y, ball.pos.z))
    sleep(0.03)
