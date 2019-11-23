# Axes3Ds

This module provides Axes3Ds ("Axes3D Spatial"), a drop-in replacement for
Axes3D which incorporates the improvements proposed by eric-wieser in matplotlib
issue #8896.

The purpose is to reduce the distortion when projecting 3D scenes into the 2D
image. For example, the projection of a sphere will be (closer to) a circle.
