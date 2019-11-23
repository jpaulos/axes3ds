# Axes3Ds for Matplotlib

This module provides Axes3Ds ("Axes3D spatial"), a drop-in replacement for
Matplotlib's Axes3D that incorporates the improvements proposed by eric-wieser
in Matplotlib issue [#8896](https://github.com/matplotlib/matplotlib/pull/8896).

The purpose is to reduce the distortion when projecting 3D scenes into the 2D
image when using mplot3d. For example, the projection of a sphere will be
(closer to) a circle.
