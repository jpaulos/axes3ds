"""
This module provides Axes3Ds ("Axes3D Spatial"), a drop-in replacement for
Axes3D which incorporates the improvements proposed by eric-wieser in matplotlib
issue #8896.

The purpose is to reduce the distortion when projecting 3D scenes into the 2D
image. For example, the projection of a sphere will be (closer to) a circle.

Please find included the Matplotlib Development Team's License Agreement for the
source material, which is Copyright (c) 2012- Matplotlib Development Team; All
Rights Reserved.
"""

import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

# Patch note: An update of the original implementation in proj3d.py.
def world_transformation(xmin, xmax,
                         ymin, ymax,
                         zmin, zmax, pb_aspect=None):
    """
    produce a matrix that scales homogenous coords in the specified ranges
    to [0, 1], or [0, pb_aspect[i]] if the plotbox aspect ratio is specified
    """
    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin
    if pb_aspect is not None:
        ax, ay, az = pb_aspect
        dx /= ax
        dy /= ay
        dz /= az

    return np.array([[1/dx, 0,    0,    -xmin/dx],
                     [0,    1/dy, 0,    -ymin/dy],
                     [0,    0,    1/dz, -zmin/dz],
                     [0,    0,    0,    1]])

class Axes3Ds(Axes3D):
    """
    Class Axes3Ds ("Axes3D Spatial") is a drop-in replacement for Axes3D which
    incorporates the improvements proposed by eric-wieser in matplotlib issue
    #8896.
    """

    # Patch note: A new function.
    def apply_aspect(self, position=None):
        if position is None:
            position = self.get_position(original=True)

        # in the superclass, we would go through and actually deal with axis
        # scales and box/datalim. Those are all irrelevant - all we need to do
        # is make sure our coordinate system is square.
        figW, figH = self.get_figure().get_size_inches()
        fig_aspect = figH / figW
        box_aspect = 1
        pb = position.frozen()
        pb1 = pb.shrunk_to_aspect(box_aspect, pb, fig_aspect)
        self.set_position(pb1.anchored(self.get_anchor(), pb), 'active')

    # Patch note: Overwritten to use the updated version of world_transformation
    # and the new pb_aspect value.
    def get_proj(self):
        """
        Create the projection matrix from the current viewing position.
        elev stores the elevation angle in the z plane
        azim stores the azimuth angle in the x,y plane
        dist is the distance of the eye viewing point from the object
        point.
        """
        # chosen for similarity with the initial view before gh-8896
        pb_aspect = np.array([4, 4, 3]) / 3.5

        relev, razim = np.pi * self.elev/180, np.pi * self.azim/180

        xmin, xmax = self.get_xlim3d()
        ymin, ymax = self.get_ylim3d()
        zmin, zmax = self.get_zlim3d()

        # transform to uniform world coordinates 0-1.0,0-1.0,0-1.0
        worldM = world_transformation(xmin, xmax,
                                      ymin, ymax,
                                      zmin, zmax, pb_aspect=pb_aspect)

        # look into the middle of the new coordinates
        R = pb_aspect / 2

        xp = R[0] + np.cos(razim) * np.cos(relev) * self.dist
        yp = R[1] + np.sin(razim) * np.cos(relev) * self.dist
        zp = R[2] + np.sin(relev) * self.dist
        E = np.array((xp, yp, zp))

        self.eye = E
        self.vvec = R - E
        self.vvec = self.vvec / np.linalg.norm(self.vvec)

        if abs(relev) > np.pi/2:
            # upside down
            V = np.array((0, 0, -1))
        else:
            V = np.array((0, 0, 1))
        zfront, zback = -self.dist, self.dist

        viewM = proj3d.view_transformation(E, R, V)
        projM = self._projection(zfront, zback)
        M0 = np.dot(viewM, worldM)
        M = np.dot(projM, M0)
        print('test')
        return M
