#   ICOMPOUND Inverse 2D relationship.
#   XJI = ICOMPOUND(XIJ) returns the inverted 2D transform XJI given
#   the relationship XIJ. Notice that all X's are 1x3-vectors, 
#   all angles within [0..2pi[.

#   References:
#      R. Smith, M. Self, P. Cheeseman, "Estimating Uncertain Spatial
#      Relationships in Robotics," in Autonomous Robot Vehicles, I.J.
#      Cox and G.T. Wilfong, Eds.: Springer-Verlag, 1990, pp. 167-193.
#
#   See also COMPOUND, JINV.

#   Adapted from v.1.0, 16.12.00, Kai Arras, ASL-EPFL
import numpy as np


def icompound(vij):

    xij = vij[0]
    yij = vij[1]
    phiij = vij[2]

    vji = np.ones(3)
    vji[0] = -xij*np.cos(phiij) - yij*np.sin(phiij)
    vji[1] = xij*np.sin(phiij) - yij*np.cos(phiij)
    phiji = -phiij

    if phiji < 0:
        vji[2] = phiji + 2*np.pi
    elif phiji >= 2*np.pi:
        vji[2] = phiji - 2*np.pi
    else:
        vji[2] = phiji

    return vji
