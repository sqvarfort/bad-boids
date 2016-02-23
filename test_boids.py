from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data = np.asarray(regression_data["before"])
    positions = np.array([boid_data[0], boid_data[1]])
    velocities = np.array([boid_data[2], boid_data[3]])
    boids = (positions, velocities
    new_boid_data = np.asarray(regression_data["after"])
    new_positions = np.asarray([new_boid_data[0], new_boid_data[1]])
    new_velocities = np.asarray([new_boid_data[2], new_boid_data[3]])
    new_boids = (new_positions, new_velocities)
    update_boids(boids)
    for after,before in zip(new_positions,boids[0]):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.1)
