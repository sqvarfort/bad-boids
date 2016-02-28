from argparse import ArgumentParser
import numpy as np
from boids import Boids
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import yaml

def process():
    parser = ArgumentParser(description = 'Simulate boids')
    parser.add_argument('boid_no', type = int, help = 'Number of boids')
    parser.add_argument('config_file', help = 'Configuration file')
    parser.add_argument('--example_view','-ex', help = 'View config file example', action='store_true')
    #parser.add_argument('--generate_example', '-gen', type = str, help = 'Generate config.yaml example file in current directory.')
    #parser.add_argument('--save', '-s', type =str, help = 'Save animation as .mp4 file. Input is the filename.')


    arguments = parser.parse_args()

    #   print 'Boids -- Simulating animal flocking behaviour. \n Input -h for help. '
    #gen = (x for x in args_iterate if type(x) == None)

    #for x in gen:

    if arguments.example_view:
        print 'The following is an example yaml config file. Copy the test below and past it into a file called filename.yaml. Make sure that the indentation is preserved.  \n \n - position: \n \t xmin: '"-450"' \n \t  xmax: "50" \n \t ymin: "300" \n \t ymax: "600" \n \n  - velocity: \n \t vxmin: "0" \n \t vxmax: "10" \n \t vymin: "-20"\n \t vymax: "20"'
        quit()
    """
    if arguments.generate_example:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        if not os.path.exists(__location__ + arguments.generate_example):
            os.makedirs(path)

        quit()
    """


    new_flock = Boids(arguments.boid_no, arguments.config_file)
    anim = animation.FuncAnimation(new_flock.figure, new_flock.animate, frames=50, interval=50)
    plt.show()

    """
    if arguments.save:
        filename = arguments.save + '.mp4'
        anim.save(filename)
    """

if __name__ == "__main__":
    process()
