# Here we write some tests


from mock import Mock
from nose.tools import assert_raises
import os
import yaml
import sys
from mock import patch
import numpy
from matplotlib import pyplot as plt



config_filename = os.path.join(os.path.dirname(__file__),'fixtures/config.yaml')


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from boids import Boids

def test_fly_towards_middle():
    new_flock = Boids(2, config_filename)
    # Set initial positions
    new_flock.positions[0][0] = 0
    new_flock.positions[1][0] = 0
    new_flock.positions[0][1] = 0
    new_flock.positions[1][1] = 10

    new_flock.velocities[0][0] = 0
    new_flock.velocities[0][1] = 0
    new_flock.velocities[1][0] = 0
    new_flock.velocities[1][1] = 0

    old_position_x1 = new_flock.positions[0][0]
    old_position_x2 = new_flock.positions[0][1]
    old_position_y1 = new_flock.positions[1][0]
    old_position_y2 = new_flock.positions[1][1]


    old_velocities_x1 = new_flock.velocities[0][0]
    old_velocities_x2 = new_flock.velocities[0][1]
    old_velocities_y1 = new_flock.velocities[1][0]
    old_velocities_y2 = new_flock.velocities[1][1]

    new_flock.fly_to_middle()

    assert(old_velocities_x1 == new_flock.velocities[0][0])
    assert(old_velocities_x2 == new_flock.velocities[0][1])
    assert(old_velocities_y1 < new_flock.velocities[1][0])
    assert(old_velocities_y2 > new_flock.velocities[1][1])


def test_match_speed(): # Check that velocities match. Should change in y-direction but stay constant in x-direction for input values.
    new_flock = Boids(2, config_filename)

    new_flock.positions[0][0] = 0
    new_flock.positions[1][0] = 10
    new_flock.positions[0][1] = 0
    new_flock.positions[1][1] = 10

    new_flock.velocities[0][0] = 0
    new_flock.velocities[0][1] = 0
    new_flock.velocities[1][0] = 0
    new_flock.velocities[1][1] = 10

    old_velocities_x1 = new_flock.velocities[0][0]
    old_velocities_x2 = new_flock.velocities[0][1]
    old_velocities_y1 = new_flock.velocities[1][0]
    old_velocities_y2 = new_flock.velocities[1][1]

    new_flock.match_velocity()

    assert(old_velocities_x1 == new_flock.velocities[0][0])
    assert(old_velocities_x2 == new_flock.velocities[0][1])
    assert(old_velocities_y1 < new_flock.velocities[1][0])
    assert(old_velocities_y2 > new_flock.velocities[1][1])


def test_avoid_collissions():
    new_flock = Boids(2, config_filename)

    new_flock.positions[0][0] = 0
    new_flock.positions[1][0] = 0
    new_flock.positions[0][1] = 1
    new_flock.positions[1][1] = 0

    new_flock.velocities[0][0] = 0
    new_flock.velocities[0][1] = 0
    new_flock.velocities[1][0] = 0
    new_flock.velocities[1][1] = 0

    old_velocities_x1 = new_flock.velocities[0][0]
    old_velocities_x2 = new_flock.velocities[0][1]
    old_velocities_y1 = new_flock.velocities[1][0]
    old_velocities_y2 = new_flock.velocities[1][1]

    new_flock.avoid_collisions()

    print new_flock.velocities

    assert(old_velocities_x1 > new_flock.velocities[0][0])
    assert(old_velocities_x2 < new_flock.velocities[0][1])
    assert(old_velocities_y1 == 0)
    assert(old_velocities_y2 == 0)



def test_initialise():
    with patch.object(numpy.random, 'rand') as mock_get:
        new_flock = Boids(10, config_filename)
        print mock_get.mock_calls
        mock_get.assert_called_with(2, 10)

def test_animate():
    with patch.object(Boids, 'update_boids') as mock_get:
        new_flock = Boids(2, config_filename)
        """new_flock.positions[0][0] = 0
        new_flock.positions[1][0] = 0
        new_flock.positions[0][1] = 1
        new_flock.positions[1][1] = 0"""
        new_flock.animate()
        print mock_get.mock_calls
        mock_get.assert_called_with()
