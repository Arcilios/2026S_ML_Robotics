# Computes the weights of all the particles
#
# The employed sensor model is range only
#
# Input:
# sensor_data: structure containing data[t][:]
# particles: array of dimension M x 3 containing the current particles
#    row represents a single particle (x, y, theta)
# landmarks: structure containing the landmark position and ids, see
#    read_word for the format

# Output:
# weights: M x 1 vector with particle weights computed by the
#         distance-only sensor model
#
# TODO: this is to be implemented as an exercise

import numpy as np
import numpy.random
import math
from ndlist import ndlist
from read_world import realworld
from read_data import read_data
import scipy.stats
import warnings


def measurement_model(sensor_data, particles, landmarks):
    # incude variance sigma_r here
    sigma_r = 0.5
    weights = []
    n_particles = len(particles)
    # measured landmarks and their ranges
    # obtain the landmark identities and their ranges from data
    for particle in particles:
        weight = 1.0
        for measurement in sensor_data:
            landmark_id = int(measurement[0])
            measured_range = measurement[1]
            landmark = landmarks[landmark_id-1]
            landmark_x = landmark[1]
            landmark_y = landmark[2]
            
            dx = particle[0] - landmark_x
            dy = particle[1] - landmark_y
            expected_range = np.sqrt(dx**2+dy**2)
            
            prob = scipy.stats.norm.pdf(
                measured_range,
                expected_range,
                sigma_r
            )
            
            weight *= prob 
        weights.append(weight)
    
    # weights per particle

    # obtaint the weight of each particle using the normal range pdf
    # create weights as a list: 
    weights = np.array(weights)
    normalizer = np.sum(weights)
    # calculate a normalizer variable for the sume of particle weights: TODO
 
    
    weights = weights/normalizer
    weights = np.array(weights)
    weights = weights.transpose()
    

    return weights

