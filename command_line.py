from argparse import ArgumentParser
import numpy as np
from boids import Boids
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import yaml

def process():
    parser = ArgumentParser(description = 'Simulate boids')
    parser.add_argument('boid_no', help = 'Number of boids')
    parser.add_argument('config_file', help = 'Configuration file')

    arguments = parser.parse_args()
    new_flock = Boids(int(arguments.boid_no), arguments.config_file)

    anim = animation.FuncAnimation(new_flock.figure, new_flock.animate, frames=50, interval=50)
    plt.show()


if __name__ == "__main__":
    process()
