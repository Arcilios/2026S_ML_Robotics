#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:34:37 2024

@author: sonia
"""
import numpy as np


def resample(particles, weights):
    # Returns a new set of particles obtained by performing
    # either a stochastic universal sampling,
    # according to the particle weights
    # or a basic resampling method.
    
    ## Normalize weight
    weights = weights / np.sum(weights)
    ## Generate sample points
    positions = (np.random.random() + np.arange(len(weights))) / len(weights)
    ## Find the segment of line each particle occupies
    indices = np.searchsorted(np.cumsum(weights), positions, side="left")
    ## Resample
    new_particles = particles[indices]

    return new_particles
