#Setup file
from setuptools import setup, find_packages
setup(
    name = 'Boids',
    version = '1.0.0',
    author = 'Sofia C. Qvarfort'
    description = 'Boids -- Simulating animal flocking behaviour',
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/Boids'],
    install_requires = ['argparse', 'numpy', 'matplotlib', 'random']
)
