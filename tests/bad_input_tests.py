from mock import Mock
from nose.tools import assert_raises
import os
import yaml
import sys

config_filename = os.path.join(os.path.dirname(__file__),'fixtures/config.yaml')


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from boids import Boids

# Test for bad input files, or file of bad format
def test_bad_input_file():
    with assert_raises(IOError) as exception:
        new_flock = Boids(10, 'file_that_does_not_exist')

# Test for negative boid number
def test_negative_boid_no():
    with assert_raises(ValueError) as exception:
        new_flock = Boids(-10, config_filename)

def test_zero_boids():
    with assert_raises(ValueError) as exception:
        new_flock = Boids(0, config_filename)

def test_wrong_boid_no_type():
    with assert_raises(TypeError) as exception:
        new_flock = Boids('string', config_filename)
