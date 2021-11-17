# decay, spontaneous decay simulation
import os

from vpython import *
import random

# import winsound
# works only for windows
# winsound.Beep(600, 100)

# os.system('beep -f %s -l %s' % (500, 100))
# works for linux but fits install sox
# sudo apt install sox
# os.system('play -q -n synth 0.1 sin 440')

lambda1 = 0.01  # decay constant
max = 80.
time_max = 500
seed = 6811
number = nloop = max  # initial value

# seting graph properties
graph = graph(width=600, height=450, title='<b>Spontaneous decay</b>', xtitle='<i>Time</i>',
              ytitle='<i>Number</i><sub> of collisions</sub>', foreground=color.blue,
              backgroundcoolr=color.green)

decayfunc = gcurve(color=color.cyan)
for time in arange(0, time_max + 1):  # Time loop
    for atom in arange(1, number + 1):  # Decay loop
        decay = random.random()
        if decay < lambda1:
            nloop = nloop - 1
            # os.system('play -q -n synth 0.1 sin 440')
        number = nloop
        decayfunc.plot([time, number])
        # sleep(0.01)
        rate(300)

# f1 = gcurve(color=color.cyan, fast=True)
# f1.data = [[10, 20], [30, 40], [50, 60]]
