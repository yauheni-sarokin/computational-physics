from vpython import *

scene.width, scene.height, scene.range, scene.title = 350, 300, 1.3, 'Widgets (buttons, etc.)\n'
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

scene.append_to_caption('\n radians/s \n')


def setspeed(s):
    wt.text = '{:1.2f}'.format(s.value)


sl = slider(min=0.3, max=3, value=1.5, length=220, bind=setspeed, right=15)
wt = wtext(text='{:1.2f}'.format(sl.value))

# objects we have in general
box_object = box(visible=True)
cone_object = cone(visible=False, radius=0.5)
pyramid_object = pyramid(visible=False)
cylinder_object = cylinder(visible=False, radius=0.5)
# current object
col = color.cyan
currentobject = box_object
currentobject.color = col

dt = 0.01

while True:
    rate(1 / dt)
    if running:
        currentobject.rotate(angle=sl.value * dt, axis=vector(0, 1, 0))
