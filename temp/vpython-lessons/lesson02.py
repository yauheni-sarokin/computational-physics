from vpython import *
import numpy as np

ball_radius = 5
ball = sphere(pos=vector(0, 0, 0), radius=ball_radius, color=color.orange)

counter = 0
while True:
    rate(100)
    increment = np.sin((np.pi * counter) / 100)
    # print(increment)
    ball.radius = ball_radius + increment
    counter += 1
