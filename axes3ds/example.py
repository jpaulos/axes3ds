"""
Side by side comparison of native Axes3D behavior and subclassed Axes3Ds with
aspect ratio improvement from issue #8896.  Things to note:

-- Stretch the figure window horizontally and vertically. Notice that the right
   image maintains it's original aspect ratio.

-- Rotate the figures perpendicular to the x-y plane and rotated 90 degrees (so
   it makes a diamond). Notice that the grid lines remain orthogonal in the
   right image.

-- Notice that while aspect ratio is preserved, this isn't an 'axis equal'
   behavior and the sphere isn't precisely a sphere.

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # normal mplot3d axes
from axes3ds import Axes3Ds # Axes3D subclassed to incorporate aspect ratio fix

# side by side axes to show previous and new behaviors
fig = plt.figure()
ax1 = Axes3D(fig,  [0,   0, 0.5, 1])
ax2 = Axes3Ds(fig, [0.5, 0, 0.5, 1])

# draw spheres
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax1.plot_wireframe(x, y, z, color="r")
ax2.plot_wireframe(x, y, z, color="r")

ax1.set_title('original')
ax2.set_title('fixed')

# force consistent ticks for side by side comparison
for axi in [ax1, ax2]:
    axi.set_xticks(np.linspace(-1, 1, 5))
    axi.set_yticks(np.linspace(-1, 1, 5))
    axi.set_zticks(np.linspace(-1, 1, 5))
fig
plt.show()
