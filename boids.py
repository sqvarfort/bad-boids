"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes

boid_no = 100
lower_pos_limits = np.array([100, 900])
upper_pos_limits = np.array([200,1100])
lower_vel_limits = np.array([0,-20])
upper_vel_limits = np.array([10,20])



def new_flock(count, lower_limits, upper_limits):
	width=upper_limits-lower_limits
	return lower_limits[:,np.newaxis]  + np.random.rand(2, count)*width[:,np.newaxis]


positions=new_flock(boid_no, np.array([100, 900]), np.array([200,1100]))

velocities=new_flock(boid_no, np.array([0,-20]), np.array([10,20]))

#positions=new_flock(boid_no, lower_pos_limits, upper_pos_limits)
#velocities=new_flock(boid_no, lower_vel_limits, upper_vel_limits)



boid_no = 3

boids_x=[random.uniform(-450,50.0) for x in range(boid_no)]
boids_y=[random.uniform(300.0,600.0) for x in range(boid_no)]
boid_positions = (boids_x, boids_y)

boid_x_velocities=[random.uniform(0,10.0) for x in range(boid_no)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(boid_no)]

old_boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
print len(old_boids)
boids=(positions[0], positions[1], velocities[0], velocities[1])
print len(boids)

def update_boids(boids):
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


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
