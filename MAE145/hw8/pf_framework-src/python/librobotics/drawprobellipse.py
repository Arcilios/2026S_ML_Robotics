#   DRAWPROBELLIPSE Draw elliptic probability region of a Gaussian in 2D.
#   DRAWPROBELLIPSE(X,C,ALPHA,COLOR) draws the elliptic iso-probabi-
#   lity contour of a Gaussian distributed bivariate random vector X
#   at the significance level ALPHA. The ellipse is centered at the column
#   vector X = [x, y] where C is the associated 2x2 covariance matrix. COLOR is
#   a [r g b]-vector or a color string such as 'r' or 'g'.

#   X and C can also be of size 3x1 and 3x3 respectively.

#   This version uses the inverse of the chi2 distribution from python

#   In case of a negative definite matrix C, the ellipse collapses
#   to a line which is drawn instead.

#   H = DRAWPROBELLIPSE(...) returns the graphic handle H.

#   See also DRAWELLIPSE, CHI2INVTABLE, CHI2INV.

# v.1.0-v.1.3, 97-Jan.03, Kai Arras, ASL-EPFL
# adapted from v.1.4, 03.12.03, Kai Arras, CAS-KTH: toolbox version

import numpy as np
from drawellipse import drawellipse
import math
import cmath
import scipy
from scipy import stats


def drawprobellipse(x, C, alpha, color):

    # calculate unscaled half axes
    sxx = C[0, 0]
    syy = C[1, 1]
    sxy = C[0, 1]

    # always greater
    a = np.sqrt(0.5*(sxx + syy + np.sqrt((sxx-syy)**2 + 4*sxy**2)))
    # always smaller
    b = cmath.sqrt(0.5*(sxx + syy - np.sqrt((sxx-syy)**2 + 4*sxy**2)))
    print(b)

    # remove imaginary parts in case of neg.definite C
    if a != np.real(a):
        a = np.real(a)
    if b != np.real(b):
        b = np.real(b)

    # scaling in order to reflect specified probability
    a = a * np.sqrt(scipy.stats.chi2.ppf(alpha, 2))
    b = b * np.sqrt(scipy.stats.chi2.ppf(alpha, 2))
  

    # Look where greater half axis belongs to
    if sxx < syy:
        swap = a
        a = b
        b = swap

    # calculate inclination (numerically stable)
    if sxx != syy:
        angle = 0.5*math.atan(2*sxy/(sxx - syy))
    elif sxy == 0:
        angle = 0   # angle doesn't matter
    elif sxy > 0:
        angle = np.pi/4
    elif sxy < 0:
        angle = - np.pi/4
    x[2] = angle
     
    # draw ellipse
    h = drawellipse(x, a, b, color)
    return h
