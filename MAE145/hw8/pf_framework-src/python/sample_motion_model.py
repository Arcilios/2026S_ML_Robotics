# function xnext = sample_motion_model(u, x)
#    Samples new particle poses, based on old poses and the odometry reading
#    
#    u: odometry reading (r1, t, r2) from the sensor data file
#    x: M x 3 array of old particles, each row representing a single
#       particle (x, y, theta)
#    xnext: M x 3 array with new particles obtained by propagating the old
#           particles with the motion model
#
#    NOTE: make use of the solution to exercise E2.6 here

import numpy as np
import numpy.random


def sample_motion_model(odometry, particles):
    # Samples new particle positions, based on old positions, the odometry
    # measurements and the motion noise
    
    delta_rot1, delta_trans, delta_rot2 = odometry
    
    # the motion noise parameters: [alpha1, alpha2, alpha3, alpha4]
    noise = [0.1, 0.1, 0.05, 0.05]
    
    # will generate new particle set after motion update and store here
    new_particles = [] 
    
    # "move" each particle according to
    # the odometry measurements plus sampled noise
    # to generate new particle set 
    
    # standard deviations of motion noise, use the odomotery motion model with the alphas
    alpha1, alpha2, alpha3, alpha4 = noise
    var_rot1 = alpha1 * delta_rot1**2 + alpha2 * delta_trans**2
    var_trans = alpha3 * delta_trans**2 + alpha4 * delta_rot1**2 + alpha4 * delta_rot2**2
    var_rot2 = alpha1 * delta_rot2**2 + alpha2 * delta_trans**2


    for particle in particles:
        new_particle = np.zeros(3)

        delta_rot1_hat = delta_rot1 - numpy.random.normal(0.0, np.sqrt(var_rot1))
        delta_trans_hat = delta_trans - numpy.random.normal(0.0, np.sqrt(var_trans))
        delta_rot2_hat = delta_rot2 - numpy.random.normal(0.0, np.sqrt(var_rot2))


        new_particle[0] = particle[0] + delta_trans_hat * np.cos(particle[2] + delta_rot1_hat)
        new_particle[1] = particle[1] + delta_trans_hat * np.sin(particle[2] + delta_rot1_hat)
        new_particle[2] = particle[2] + delta_rot1_hat + delta_rot2_hat

        # append result to newparticles list
        new_particles.append(new_particle)
    new_particles = np.array(new_particles)
    return new_particles
