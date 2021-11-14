from vpython import *

ball_radius = 0.5
# ball with trail
ball = sphere(pos=vector(-5, 0, 0), radius=ball_radius, color=color.cyan, make_trail=True)
wall_thickness = 0.2
wallRcolor = color.green
wallR = box(pos=vector(6, 0, 0), size=vector(wall_thickness, 12, 12), color=wallRcolor)
wallLcolor = color.blue
wallL = box(pos=vector(-6, 0, 0), size=vector(wall_thickness, 12, 12), color=wallLcolor)
wallTcolor = color.magenta
wallT = box(pos=vector(0, 6, 0), size=vector(12, wall_thickness, 12), color=wallTcolor)
wallBColor = color.orange
wallB = box(pos=vector(0, -6, 0), size=vector(12, wall_thickness, 12), color=wallBColor)
wallBackcolor = color.rgb_to_hsv(vector(190 / 255, 50 / 255, 195 / 255))
wallBack = box(pos=vector(0, 0, -6), size=vector(12, 12, wall_thickness),
               color=wallBackcolor)
wallFrontColor = color.orange
wallFront = box(pos=vector(0, 0, 6), size=vector(12, 12, wall_thickness), color=wallFrontColor, opacity=0.3)

# we specify x, y, z component of tje ball's velocity
ball.velocity = vector(25, 5, 15)
# ball.velocity = vector(25, 0, 0)
# visualize velocity vector with arrow
vscale = 0.1
varr = arrow(pos=ball.pos, axis=ball.velocity * vscale, color=color.yellow)

# time interval between snaphots delta t
deltat = 0.005
# time to start
t = 0
# turn off autoscaling
scene.autoscale = False

print(wallFront.pos.z)
print(wallBack.pos.z)

while t < 5:
    rate(100)
    collision = False
    if ball.pos.x + ball_radius > wallR.pos.x - wall_thickness or \
            ball.pos.x - ball_radius < wallL.pos.x + wall_thickness:
        ball.velocity.x = -ball.velocity.x
        collision = True
    if ball.pos.y + ball_radius > wallT.pos.y - wall_thickness or \
            ball.pos.y - ball_radius < wallB.pos.y + wall_thickness:
        ball.velocity.y = -ball.velocity.y
        collision = True
    if ball.pos.z - ball_radius < wallBack.pos.z + wall_thickness or \
            ball.pos.z + ball_radius > wallFront.pos.z - wall_thickness:
        ball.velocity.z = -ball.velocity.z
        collision = True



    ball.pos = ball.pos + ball.velocity * deltat
    varr.pos, varr.axis = ball.pos, ball.velocity * vscale

    t = t + deltat
