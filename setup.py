from setuptools import setup

setup(name='axes3ds',
      version='0.0',
      description='A patched version of Matplotlib Axes3D with less projection distortion.',
      url='https://github.com/jpaulos/axes3ds',
      author='Jimmy Paulos',
      author_email='jpaulos@seas.upenn.edu',
      license='PSF',
      packages=['axes3ds'],
      install_requires=[
          'matplotlib',
          'numpy',
      ],
      zip_safe=False)
