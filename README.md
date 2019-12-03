# Axes3Ds for Matplotlib

This module provides Axes3Ds ("Axes3D spatial"), a drop-in replacement for Matplotlib's Axes3D that incorporates the improvements proposed by eric-wieser in Matplotlib issue [#8896](https://github.com/matplotlib/matplotlib/pull/8896). It is simply a subclass of Axes3D replacing one or two member functions.

The purpose is to reduce the distortion when projecting 3D scenes into the 2D image when using mplot3d, especially as the aspect ratio of the figure is changed. This makes it possible to draw a 3D sphere that correctly projects to approximately a circle even as the figure window is resized. True "axis equal" behavior could presumably be implemented on top of this. 

![Horizontal](https://user-images.githubusercontent.com/2522557/70083386-48ffd100-15da-11ea-9a0d-ffc5b6c3fd49.png)

![Vertical](https://user-images.githubusercontent.com/2522557/70083395-4e5d1b80-15da-11ea-8c9e-608da46d19c3.png)

![Orthogonol](https://user-images.githubusercontent.com/2522557/70083404-51580c00-15da-11ea-965c-5c7768af1116.png)
