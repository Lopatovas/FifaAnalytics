from setuptools import setup

setup(
   name='Fifa-Analytics',
   version='1.0',
   description='Tool for analizing players in fifa',
   author='Edgaras Lopatovas',
   author_email='lopatovas@gmail.com',
   packages=['Fifa-Analytics'],
   install_requires=['span', 'pandas', 'numpy', 'matplotlib', 'seaborn'],
)