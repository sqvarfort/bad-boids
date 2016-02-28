from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from boids.boids import Boids

def test_bad_boids_regression():
#    open(os.path.join(os.path.dirname(__file__),'boids.py'))
    config_filename = os.path.join(os.path.dirname(__file__),'fixtures/config.yaml')
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture.yaml')))

    boids = Boids(10, config_filename)
    boid_data = np.asarray(regression_data["before"])
    boids.positions = np.array([boid_data[0], boid_data[1]])
    boids.velocities = np.array([boid_data[2], boid_data[3]])
    boids.update_boids()

    new_boid_data = np.asarray(regression_data["after"])
    new_positions = np.asarray([new_boid_data[0], new_boid_data[1]])
    new_velocities = np.asarray([new_boid_data[2], new_boid_data[3]])
    new_boids = (new_positions, new_velocities)


    for after,before in zip(new_positions,boids.positions):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.06)
