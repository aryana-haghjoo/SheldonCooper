# -*- coding: utf-8 -*-
"""SC_time_evolution.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y7Itl9CuwelIuhgk3-kGsLG8SdLsXR19
"""

#time evolution for the Sheldon Cooper N Body Simulation

import numpy as np
import scipy
import matplotlib.pyplot as plt
# import pint

# Constants
dt = 1  # Time step in years
T = 100  # Total time in years
step = int(T / dt)  # Number of steps

# Particle system dimensions
n = 2  # Number of particles (for testing)
r_i = np.ones((3, n))  # Initial position (3 coordinates for each particle)
v_i = np.ones((3, n))  # Initial velocity (3 coordinates for each particle)
a_i = np.ones((3, n))  # Initial acceleration (3 coordinates for each particle)



# Evolve velocity function
def evolve_velocity(v, a):
    """Evolves the velocity of each particle.
    Each v_i and a_i is a 3xn numpy array representing x, y, z coordinates for n particles."""
    v_new = v + a * dt  # Update velocity using v = v0 + at
    return v_new        # Return updated velocity

# Evolve position function
def evolve_position(r, v):
    """Evolves the position of each particle.
    Each r_i and v_i is a 3xn numpy array representing x, y, z coordinates for n particles."""
    r_new = r + v * dt  # Update position using r = r0 + vt
    return r_new        # Return updated position


# Initialize a matrix to store positions, velocities, and accelerations over time
matrix = np.empty((n, step, 3))   # Empty matrix of shape (n particles, steps, 3 coordinates)
arr_3x1 = np.ones((3, 1))         # 3x1 array of ones
matrix[:, :, :] = arr_3x1.T       # Assuming arr_3x1 is predefined and is a 3x1 array for initialization

# Duplicate matrix for velocity, acceleration, and position
velocity = matrix.copy()                # Matrix to store velocity over time
position = matrix.copy()                # Matrix to store position over time
acceleration = matrix.copy()            # Matrix to store acceleration over time

# Time evolution loop
for s in range(step):   # Iterate through each time step
  # Store current velocity, acceleration, and position for each particle at time step s
  velocity[:,s,:] = v_i.T
  acceleration[:,s,:] = a_i.T
  position[:,s,:] = r_i.T

  # Evolve velocity and position using the current state
  v_temp = evolve_velocity(v_i,a_i)          # Update velocity
  r_i = evolve_position(r_i,v_i)             # Update position based on the current velocity
  v_i = v_temp                               # Update the velocity for the next iteration
# a_i = force_func(mass,r_i)        # Update acceleration based on the forces

print(v_i,r_i)

#import scipy.integrate.quad as quad

#quad(func,t_i,t_f)

 # Integrates 'func' over the interval [t_i, t_f]
#quad(force_func(mass,positions),t_i,t_f) #output change in velocity a*dt


#def evolve_velocity(v,a,mass):
 # """evolves the velocity of each particle
   #  each v_i and a_i is a 3x1 numpy array representing an x,y,z coordinate"""
 # v_new = v + quad(force_func(mass,positions)/mass,t_i,t_f)   # Only take the integral result
  # v = v_new   # Return the updated velocity
 # return v_new

#def evolve_position(r,v):
#  r_new = r + quad(evolve_velocity())
  # r = r_new
#  return r_new

#for