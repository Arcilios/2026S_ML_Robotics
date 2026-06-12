#   COMPOUND Compound 2D relationships.
#   XIJ = COMPOUND(XI,XJ) returns the compound relationship of the two
#   two dimensional transforms XI and XJ which are arranged head-to-
#   tail. All X's are arrays 1 times 3, all angles within [0..2pi[.
#
#   References:
#      R. Smith, M. Self, P. Cheeseman, "Estimating Uncertain Spatial
#      Relationships in Robotics," in Autonomous Robot Vehicles, I.J.
#      Cox and G.T. Wilfong, Eds.: Springer-Verlag, 1990, pp. 167-193.
#
#   See also ICOMPOUND, J1COMP, J2COMP.

#   python version of  Kai Arras' compound.m, ASL-EPFL

import numpy as np


def compound(vij, vjk):
    xij = vij[0]
    xjk = vjk[0]
    yij = vij[1]
    yjk = vjk[1]
    phiij = vij[2]
    phijk = vjk[2]

    vik = np.array(range(3))

    vik[0] = xjk*np.cos(phiij) - yjk*np.sin(phiij) + xij
    vik[1] = xjk*np.sin(phiij) + yjk*np.cos(phiij) + yij
    phiik = phiij + phijk

    if phiik < 0:
        vik[2] = phiik + 2*np.pi
    elif phiik >= 2*np.pi:
        vik[2] = phiik - 2*np.pi
    else:
        vik[2] = phiik

    return vik
