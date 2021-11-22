# graph
from vpython import *
from numpy import arange

gd = graph(width=600, height=450, title='<b>Test</b>', xtitle='<i>x</i>',
           ytitle='<i>x</i><sup>2</sup>', foreground=color.blue,
           backgroundcoolr=color.green, xmin=-0, xmax=9,
           ymin=-6, ymax=6)
f1 = gcurve(color=color.cyan, fast=True)  # a graphics curve)
f2 = gvbars(delta=0.05, color=color.blue)
for x in arange(0, 8.05, 0.1):  # x goes from 0 to 8
    # sleep(0.01)
    f1.plot(x, 5 * cos(2 * x) * exp(-0.2 * x))
    f2.plot(x, 4 * cos(0.5 * x) * exp(-0.1 * x))  # vbars

scene.width, scene.height, scene.range, scene.title = 10, 10, 1.3, 'Widgets (buttons, ' \
                                                                   'etc.)\n'

running = True


def Run(b):
    global running
    running = not running
    if running:
        b.text = 'Pause'
    else:
        b.text = 'Run'


# Create button to control pause
button(text='Pause', pos=scene.title_anchor, bind=Run)

# scene.append_to_caption('\n radians/s \n')
# c = controls(x=500, y=0, width=200, height=200)
dt = 0.1
while True:
    rate(1 / dt)
