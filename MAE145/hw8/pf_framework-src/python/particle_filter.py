# This is the main particle filter. This script calls all the required
# functions in the correct order.

# You can disable the plotting or change the number of steps the filter
# runs for to ease the debugging. You should however not change the order
# or calls of any of the oter lines, as it might break the framework.

# If you are unsure about the input and return values of functions you
# should read their documentation which tells you the expected dimensions.
# You will often encounter "M" in the dimensions which is the number of
# particles used.

# Make librobotics available:
#   add path('librobotics') in PYTHONPATH manager
import numpy as np
import numpy.random
import math
from read_world import realworld
from read_data import read_data
from init_particles import initialize_particles
from measurement_model import measurement_model
from landmarks import realworld
from ndlist import ndlist
from sample_motion_model import sample_motion_model
from measurement_model import measurement_model
from mean_position import mean_position
from plot_state import plot_state
import warnings
from resample_universal import resample



# Read world data, i.e. landmarks
landmarks = realworld("../data/world.text")

# Read sensor readings, i.e. odometry and range-bearing sensor
data = read_data("../data/sensor_data.text")

# Initialize particles and weights
particles = initialize_particles(500)
weights = np.ones(500)/500


# Generate visualization plot of the initial state of the filter
plot_state(particles, weights, landmarks, -1)

# Perform filter update for each odometry, observation pair read from the
# data file --- To be done:

for t in range(30):  # can do until 330 from the data file
    # Propagate the old particles according to the motion model
    # fill out the sample_motion_model py file, 
    # extract the odometry information from data
    
    new_particles = sample_motion_model(data[t][0], particles)

    # Compute the weights of the new particles using a distance-only sensor
    # model. Extract this info from 'data'. You can start with the range and bearing sensor model to try
    # the filter out
    weights = measurement_model(data[t][1:], new_particles, landmarks)

    # Normalize the weights of particles
    weights = weights/sum(weights)

    # Create a new generation of particles by sampling particles from the
    # old set according to their weight.
    # Using a simple resampling may lead to particle deprivation, you need to
    # use a more advanced stochastic sampling method
    particles = resample(new_particles, weights)
    # Generate visualization plots of the current state of the filter
    plot_state(particles, weights, landmarks, t)

# Display the final state estimate
print("Final pose: ")
print(mean_position(particles, weights))
