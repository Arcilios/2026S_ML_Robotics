#NORMANGLE Put angle into a two-pi interval.
#   AR = NORMANGLE(A,MIN) puts angle A into the interval
#   [MIN..MIN+2*pi[. If A is Inf, Inf is returned.
#
#   See also DIFFANGLE.

# v.1.0, Dec. 2017, S. Martinez from a Kai Arras version CAS-KTH: accel. with profiler


import math
import numpy as np


def normalangle(a,mina):
    if a < math.inf:
        while a >= mina + 2* np.pi:
            a = a - 2*np.pi
        while a < mina:
            a = a + 2*np.pi
    else:
        a = math.inf
    return a
        
 
