from vpython import *
from vpython import vector as v

c = curve()
# c.append(v(-1, -1, 0), v(1, -1, 0))
v1, v2, v3, v4, v5 = v(-1, -1, 0), v(1, -1, 0), v(1, 1, 0), v(-1, 1, 0), v(-1, -1, 0)
# c = curve(v(-1, -1, 0), v(1, -1, 0))
# c.append(v(1, 1, 0), v(-1, 1, 0), v(-1, -1, 0), color=color.cyan, radus=0.3)
c = curve(pos=[v1, v2], color=color.green, radius=0.05)
c = curve(pos=[v2, v3], color=color.blue, radius=0.02)

p3 = dict(pos=v3, color=color.red, radius=0.03)
p4 = dict(pos=v4, color=color.orange, radius=0.04)
curve(p3, p4)

# c = curve(retain=150)
# c.append(pos=v5, retain=30)
