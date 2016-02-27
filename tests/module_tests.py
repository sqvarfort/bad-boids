# Here we write some tests


from mock import Mock
from nose.tools import assert_raises
import os
import yaml
import sys



config_filename = os.path.join(os.path.dirname(__file__),'fixtures/config.yaml')


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from boids import Boids

def test_fly_towards_middle():
    new_flock = Boids(2, config_filename)
    # Set initial positions
    new_flock.positions[0][0] = 0
    new_flock.positions[1][0] = 0
    new_flock.positions[0][1] = 10
    new_flock.positions[1][1] = 10

    old_position_x1 = new_flock.positions[0][0]
    old_position_x2 = new_flock.positions[0][1]
    old_position_y1 = new_flock.positions[1][0]
    old_position_y2 = new_flock.positions[1][1]

    new_flock.fly_to_middle()
    assert(old_position_x1 < new_flock.positions[0][0])
    assert(old_position_x2 < new_flock.positions[0][1])

def test_match_speed():
    something = 0

def test_initialise():



def test_collission_detection():

# Need negative testing

def test_animate():
#    with patch.object(animate, 'get') as mock_get:
