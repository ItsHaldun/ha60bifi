from distutils.core import setup
from setuptools import find_packages
setup(name='ha60bifi',
      version='0.1',
      author='DSSS',
      author_email='haldun.bucak@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets', 'matplotlib.pyplot'])