# another trial to have graph with controls
from vpython import *
from numpy import array, zeros

# Just dont touch it
# ------------------------------------------------------------------>
scene.height = 1
running = True
update = False
# ------------------------------------------------------------------>

# Graph created here
# ------------------------------------------------------------------>
gd = graph(width=500, height=500, title='<b>Spline fit</b>', xtitle='<i>x</i>',
           ytitle='<i>y</i><sup>2</sup>', foreground=color.blue,
           backgroundcoolr=color.green,
           # xmin=-0, xmax=9, ymin=-6, ymax=6
           )
# ------------------------------------------------------------------>

# G curve & dots
# ------------------------------------------------------------------>
funct1 = gdots(color=color.orange)
funct2 = gdots(color=color.red)


# f1 = gcurve(color=color.cyan, fast=True)  # a graphics curve)
# f2 = gvbars(delta=0.05, color=color.blue)
# for x in arange(0, 8.05, 0.1):  # x goes from 0 to 8
# sleep(0.01)
# f1.plot(x, 5 * cos(2 * x) * exp(-0.2 * x))
# f2.plot(x, 4 * cos(0.5 * x) * exp(-0.1 * x))  # vbars


# ------------------------------------------------------------------>


# Maybe delete it later
# ------------------------------------------------------------------>
def Run(b):
    global running, update
    running = not running
    update = True
    if running:
        b.text = 'Pause'
    else:
        b.text = 'Run'


# ------------------------------------------------------------------>


# Create button to control pause and slider
# ------------------------------------------------------------------>
button(text='Pause', pos=scene.title_anchor, bind=Run)

scene.append_to_caption('\n radians/s \n')


def setspeed(s):
    global update
    wt.text = '{:1.2f}'.format(s.value)
    update = True


sl = slider(min=2, max=100, value=10, length=500, bind=setspeed, right=15)
wt = wtext(text='{:1.2f}'.format(sl.value))

# actual program from the book
# ------------------------------------------------------------------>
x_arr = array([0., 0.12, 0.25, 0.37, 0.5, 0.62, 0.75, 0.87, 0.99])
y = array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
n, np = 9, 15

# Initialize
y2, u = zeros((n), float), zeros((n), float)


# ------------------------------------------------------------------>

# ------------------------------------------------------------------>

# function is triggered once slider is moved
def do_update():
    funct1.delete()
    funct2.delete()
    # global x
    Nfit = int(sl.value)
    # print(Nfit)
    for i in range(0, n):
        funct1.plot(pos=(x_arr[i], y[i]))
        funct1.plot(pos=(1.01 * x_arr[i], 1.01 * y[i]))
        funct1.plot(pos=(0.99 * x_arr[i], 0.99 * y[i]))

    yp1 = (y[1] - y[0]) / (x_arr[1] - x_arr[0]) - (y[2] - y[1]) \
          / (x_arr[2] - x_arr[1]) + (y[2] - y[0]) / (x_arr[2] - x_arr[0])
    ypn = (y[n - 1] - y[n - 2]) / (x_arr[n - 1] - x_arr[n - 2]) - (y[n - 2] - y[n - 3]) / (
            x_arr[n - 2] - x_arr[n - 3]) + (y[n - 1] - y[n - 3]) / (x_arr[n - 1] - x_arr[n - 3])
    if yp1 > 0.99e30:
        y2[0], u[0] = 0., 0.
    else:
        y2[0] = -0.5
        u[0] = (3. / (x_arr[1] - x_arr[0])) * ((y[1] - y[0]) / (x_arr[1] - x_arr[0]) - yp1)
    for i in range(1, n - 1):
        sig = (x_arr[i] - x_arr[i - 1]) / (x_arr[i + 1] - x_arr[i - 1])
        p = sig * y2[i - 1] + 2.
        y2[i] = (sig - 1.) / p
        u[i] = (y[i + 1] - y[i]) / (x_arr[i + 1] - x_arr[i]) - (y[i] - y[i - 1]) / (x_arr[i] - x_arr[i - 1])
        u[i] = (6. * u[i] / (x_arr[i + 1] - x_arr[i - 1]) - sig * u[i - 1]) / p
    if (ypn > 0.99e30):
        qn = un = 0.
    else:
        qn = 0.5
        un = (3 / (x_arr[n - 1] - x_arr[n - 2])) * (ypn - y[n - 1] - y[n - 2]) / (x_arr[n - 1] - x_arr[n - 2])
    y2[n - 1] = (un - qn * u[n - 2]) / (qn * y2[n - 2] + 1.)
    for k in range(1, Nfit + 2):
        xout = x_arr[0] + (x_arr[n - 1] - x_arr[0]) * (i - 1) / Nfit
        klo = 0
        khi = n - 1
        while khi - klo > 1:
            k = khi + klo >> 1
            if x_arr[k] > xout:
                khi = k
            else:
                klo = k
        h = x_arr[khi] - x_arr[klo]
        if x_arr[k] > xout:
            khi = k
        else:
            klo = k
        h = x_arr[khi] - x_arr[klo]
        a = (x_arr[khi] - xout) / h
        b = (xout - x_arr[klo]) / h
        yout = a * y[klo] + b * y[khi] + ((a * a * a - a) * y2[klo] + (b * b * b - b) * y2[khi]) * h * h / 6
        funct2.plot(pos=(xout, yout))
    # f1.delete()


# infinite loop
# ------------------------------------------------------------------>
dt = 0.1
do_update()
while True:
    rate(1 / dt)
    if update:
        # print('update')
        do_update()
        update = False
# ------------------------------------------------------------------>
