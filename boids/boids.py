"""
Boids
-----------------
Simulates the behaviour of flocking animals, such as starlings.
This file contains the Boid class.

Adapted from a deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml
import os


class Boids(object):
	def __init__(self, boid_no, config):
		# Open config file, raise exception if yaml cannot reaad the text.
		try:
			input_data = yaml.load(open(os.path.join(os.path.dirname(__file__),config)))
		except IOError:
			print 'Could not read file.'
			raise IOError
			quit()

		if boid_no == 0:
			raise ValueError
			quit()

		# Assign config file values to variables
		position_values = input_data[0]
		velocity_values = input_data[1]

		# Define input paramters
		self.lower_pos_limits = np.array([int(position_values['xmin']), int(position_values['ymin'])])
		self.upper_pos_limits = np.array([int(position_values['xmax']), int(position_values['ymax'])])
		self.lower_vel_limits = np.array([int(velocity_values['vxmin']), int(velocity_values['vymin'])])
		self.upper_vel_limits = np.array([int(velocity_values['vxmax']), int(velocity_values['vymax'])])

		# Make 2xN arrays with positions[0] = x-values and positions[1] = y-values
		self.positions=self.initialise(boid_no, self.lower_pos_limits, self.upper_pos_limits)
		self.velocities=self.initialise(boid_no, self.lower_vel_limits, self.upper_vel_limits)

		# Create figure
		self.figure=plt.figure()
		self.axes=plt.axes(xlim=(int(self.lower_pos_limits[0]),int(self.upper_pos_limits[0])+1000), ylim=(int(self.lower_pos_limits[1])-500,int(self.upper_pos_limits[1])+500)) #Axes will adapt with input parameters
		self.scatter=self.axes.scatter(self.positions[0,:],self.positions[1,:])
		plt.ylabel('$y$')
		plt.title('Boids')
		plt.xlabel('$x$')
		plt.rcParams.update({'font.size': 40})

	def initialise(self, count, lower_limits, upper_limits): # Initialise random values for positions and velocities over the specified range
		width=upper_limits-lower_limits
		return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])


	def calculate_separations(self):
		self.separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis] # Use broacast to calculate a matrix of separations
		self.squared_displacements = self.separations * self.separations
		self.square_distances = np.sum(self.squared_displacements, 0)

	def fly_to_middle(self): # Make the Boids fly towards the middle
		middle = np.mean(self.positions,1) # Calculate middle of flcok
		dir_to_middle = self.positions-middle[:, np.newaxis]
		middle_strength = 0.01
		self.velocities -= dir_to_middle*middle_strength

	def avoid_collisions(self): # Include collission detection
		self.calculate_separations() #update separation matrix
		alert_distance = 100
		far_away = self.square_distances > alert_distance # Create logical array
		separations_if_close = np.copy(self.separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		self.velocities += np.sum(separations_if_close,1) # Update velocities

	def match_velocity(self):
		self.calculate_separations() #update separation matrix
		
		velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis] #Get 10x10 matrix with the difference between every bird
		formation_flying_distance = 10000 # Set limit to the distance that the birds want
		formation_flying_strength = 0.125
		very_far = self.square_distances > formation_flying_distance # Create boolean matrix
		velocity_differences_if_close = np.copy(velocity_differences)
		velocity_differences_if_close[0,:,:][very_far] = 0
		velocity_differences_if_close[1,:,:][very_far] = 0
		self.velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength # update velocities

	def update_boids(self): # Apply all methods
		# Call all the methods used
		self.fly_to_middle()
		self.avoid_collisions()
		self.match_velocity()
		dt = 1 # Time constant to define iteration steps. This is probably inefficient
		self.positions += dt * self.velocities # Update velocities


	def animate(self, frame): # Parameters for the animation. Note that frame cannot be removed.
		self.update_boids()
	   	self.scatter.set_offsets(zip(self.positions[0, :],self.positions[1, :]))
