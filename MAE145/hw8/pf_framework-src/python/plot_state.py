#    plot_state(particles, weights, landmarks, timestep)
#   Visualizes the state of the particle filter.

# The resulting plot displays the following information:
# - landmark positions
# - particle positions
# - estimate of the filter state

# particles: M x 3 matrix with the current particles
# weights: M x 1 vector with the particle weights
# timestep: current step in the filtering process
import numpy as np
import matplotlib.pyplot as plt
from mean_position import mean_position
#from drawrobot import drawrobot


def plot_state(newparticles, weights, landmarks, timestep):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # plt.plot()
    plt.grid(True)
    # do the particles first
    plt.plot(newparticles[:, 0], newparticles[:, 1], '.')
    long = len(landmarks)
    for k in range(long):
        plt.plot(landmarks[k][1], landmarks[k][2], 'o')
    # do the weights
    if sum(weights) > 0:
        meanposition = mean_position(newparticles, weights)
    else:
        n_particles = len(newparticles)
        weights = np.ones(n_particles)*(1/n_particles)
        meanposition = mean_position(newparticles, weights)
    
    deg = meanposition[2]*360/(2*np.pi)
    plt.plot(meanposition[0],meanposition[1], marker=(3, 0, deg-90), markersize=7, color='r', linestyle='None')
    #drawrobot(meanposition, 'r', 3)#, 0.3, 0.3)
    plt.xlim(-5, 11)
    plt.ylim(-5, 11)

    # the following saves the figure to a timestamped png file:
    plt.savefig("../plots/pf_" + str(timestep + 1) + "timestep03d.png")
    plt.close(fig)
