# graph
from vpython import *
from numpy import arange

gd = graph(width=600, height=450, title='<b>Test</b>', xtitle='<i>x</i>',
           ytitle='<i>x</i><sup>2</sup>', foreground=color.blue,
           backgroundcoolr=color.green, xmin=-20, xmax=50,
           ymin=-1, ymax=10)
f1 = gcurve(color=color.cyan, fast=True)  # a graphics curve)
f2 = gvbars(delta=0.05, color=color.blue)
for x in arange(0, 8.05, 0.1):  # x goes from 0 to 8
    sleep(0.1)
    f1.plot(x, 5 * cos(2 * x) * exp(-0.2 * x))
    f2.plot(x, 4 * cos(0.5 * x) * exp(-0.1 * x))  # vbars

# f1.data = [[10, 20], [30, 40], [50, 60]]
