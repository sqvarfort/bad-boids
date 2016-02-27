# File to capture fixtures
from boids import Boids
import copy
import yaml
import numpy as np
import os

filename = os.path.join(os.path.dirname(__file__),'new_fixtures.yaml')
#yaml.load(open(filename))

new_flock = Boids(10, 'config.yaml')
old_positions = copy.deepcopy(new_flock.positions)
old_velocities = copy.deepcopy(new_flock.velocities)

with open(filename, "w") as f:
        yaml.dump(old_positions, f, default_flow_style=True)
        yaml.dump(old_velocities, f, default_flow_style=True)


doc = yaml.load(open(filename))

print doc


#npzfile = np.load('new_fixtures.npz')
#np.save(npzfile, old_positions)
#np.save('new_fixtures.yml', old_velocities)
#test = np.load('new_fixtures.npz')
