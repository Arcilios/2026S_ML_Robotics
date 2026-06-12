# Define a function mean_position 
# Returns a single estimate of filter state=(x, y, theta) based
# on the particle cloud.

# Input:
# particles: array of dimension M x 3 representing the particles
# weights: vector of dimension M x 1 containing the particle weights

# Output:
# a 3 x 1 vector with the estimate of the filter state / pose

import numpy as np

def mean_position(particles,weights):
    mean_pose = np.zeros(3)

    mean_pose[0] = np.sum(particles[:, 0] * weights)
    mean_pose[1] = np.sum(particles[:, 1] * weights)

    sin_sum = np.sum(np.sin(particles[:, 2]) * weights)
    cos_sum = np.sum(np.cos(particles[:, 2]) * weights)
    mean_pose[2] = np.arctan2(sin_sum, cos_sum)

    return mean_pose




