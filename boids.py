"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes


boid_no = 10
lower_pos_limits = np.array([-450, 300.0])
upper_pos_limits = np.array([50,600])
lower_vel_limits = np.array([0,-20])
upper_vel_limits = np.array([10,20])


# Note that lower_limits[x-limit, y-limit]
# and the same for upper limits
def initialise(count, lower_limits, upper_limits):
	width=upper_limits-lower_limits
	return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])


#positions=new_flock(boid_no, lower_pos_limits, upper_pos_limits)
#velocities=new_flock(boid_no, lower_vel_limits, upper_vel_limits)

#boids=(positions[0], positions[1], velocities[0], velocities[1])


def update_boids(boids):
	positions = boids[0]

	velocities = boids[1]
#	print positions
#	print ' ----------------------------'
#	print velocities
	dt = 1
	# Fly in straight line
	#positions += velocities * dt
	# Fly towards the middle
	middle = np.mean(positions,1)
	dir_to_middle = positions-middle[:, np.newaxis]
	middle_strength = 0.01
	velocities -= dir_to_middle*middle_strength
	#Avoiding collissions
	separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	squared_displacements = separations * separations
	square_distances = np.sum(squared_displacements, 0)
	alert_distance = 100
	far_away = square_distances > alert_distance
	separations_if_close = np.copy(separations)
	separations_if_close[0,:,:][far_away] = 0
	separations_if_close[1,:,:][far_away] = 0
	velocities += np.sum(separations_if_close,1)

	# Match velocity with nearby birds
	velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis] #Get 10x10 matrix with the difference between every bird

	formation_flying_distance = 10000 # Set limit to the distance that the birds want
	formation_flying_strength = 0.125
	very_far = square_distances > formation_flying_distance
	velocity_differences_if_close = np.copy(velocity_differences)
	velocity_differences_if_close[0,:,:][very_far] = 0
	velocity_differences_if_close[1,:,:][very_far] = 0
	velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength
	positions += velocities

	"""
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]
"""


positions=initialise(boid_no, lower_pos_limits, upper_pos_limits)
velocities=initialise(boid_no, lower_vel_limits, upper_vel_limits)
boids = (positions, velocities)

#print positions

figure=plt.figure()

axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
#scatter=axes.scatter(boids[0],boids[1])
scatter=axes.scatter(positions[0,:],positions[1,:])
#plt.ylabel('Resistance / $\Omega$')
plt.title('Boids')
#plt.xlabel('B-field / Tesla')
plt.rcParams.update({'font.size': 22})



def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(positions[0, :],positions[1, :]))

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
