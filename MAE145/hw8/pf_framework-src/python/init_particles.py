# Returns a set of randomly initialized particles
#
# Creates "count" particles normally distributed around (0,0) with a
# standard deviation of 1
# The returned matrix has the dimension count x 3, where each row in
# the matrix represents the (x, y, theta) values of a single particle

import numpy as np
import numpy.random


def initialize_particles(count):
    particles = np.zeros((count, 3))

    particles[:, 0] = np.random.normal(0, 1, count)
    particles[:, 1] = np.random.normal(0, 1, count)
    particles[:, 2] = 2 * np.pi * np.random.rand(count)

    return particles
