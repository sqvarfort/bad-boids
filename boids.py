"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes


class Boids(object):
	def __init__(self, boid_no):

		self.lower_pos_limits = np.array([-450, 300.0])
		self.upper_pos_limits = np.array([50,600])
		self.lower_vel_limits = np.array([0,-20])
		self.upper_vel_limits = np.array([10,20])
		upper_pos_limits = np.copy(self.upper_pos_limits)
		lower_pos_limits = np.copy(self.lower_pos_limits)
		lower_vel_limits = np.copy(self.lower_vel_limits)
		upper_vel_limits = np.copy(self.upper_vel_limits)
		self.boid_no = boid_no
		self.positions=self.initialise(boid_no, lower_pos_limits, upper_pos_limits)
		self.velocities=self.initialise(boid_no, lower_vel_limits, upper_vel_limits)
		#positions = Boids.positions
		#velocities = BoidsB.velocities
		self.boids = (self.positions, self.velocities)

		self.figure=plt.figure()
		self.axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		self.scatter=self.axes.scatter(self.positions[0,:],self.positions[1,:])

		plt.ylabel('$y$')
		plt.title('Boids')
		plt.xlabel('$x$')
		plt.rcParams.update({'font.size': 40})

		"""
		self.figure=plt.figure()
		self.axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		self.scatter=self.axes.scatter(self.positions[0,:],self.positions[1,:])
		plt.ylabel('$y$')
		plt.title('Boids')
		plt.xlabel('$x$')
		plt.rcParams.update({'font.size': 40})
		"""


	def initialise(self, count, lower_limits, upper_limits):
		width=upper_limits-lower_limits
		return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])


	def update_boids(self, boids):
		# Fly towards the middle
		middle = np.mean(self.positions,1)
		dir_to_middle = self.positions-middle[:, np.newaxis]
		middle_strength = 0.01
		self.velocities -= dir_to_middle*middle_strength
		#Avoiding collissions
		separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
		squared_displacements = separations * separations
		square_distances = np.sum(squared_displacements, 0)
		alert_distance = 100
		far_away = square_distances > alert_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		self.velocities += np.sum(separations_if_close,1)

		# Match velocity with nearby birds
		velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis] #Get 10x10 matrix with the difference between every bird
		formation_flying_distance = 10000 # Set limit to the distance that the birds want
		formation_flying_strength = 0.125
		very_far = square_distances > formation_flying_distance
		velocity_differences_if_close = np.copy(velocity_differences)
		velocity_differences_if_close[0,:,:][very_far] = 0
		velocity_differences_if_close[1,:,:][very_far] = 0
		self.velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength
		dt = 1
		self.positions += dt * self.velocities


	def animate(self, frames):
		self.update_boids(self.boids)
	   	self.scatter.set_offsets(zip(self.positions[0, :],self.positions[1, :]))

#if __name__ == "__main__":
new_flock = Boids(1000)

anim = animation.FuncAnimation(new_flock.figure, new_flock.animate, frames=50, interval=50)
plt.show()
