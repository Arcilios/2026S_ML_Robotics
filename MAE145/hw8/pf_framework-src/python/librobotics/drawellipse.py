#   DRAWELLIPSE Draw ellipse.
#   DRAWELLIPSE(X,A,B,COLOR) draws an ellipse at X = [x, y, theta]
#   with half axes A and B. Theta is the inclination angle of A,
#   regardless if A is smaller or greater than B. COLOR is a
#   [r g b]-vector or a color string such as 'r' or 'g'.
#
#   H = DRAWELLIPSE(...) returns the graphic handle H.
#
#   See also DRAWPROBELLIPSE.

# v.1.0-v.1.1, Aug.97-Jan.03, Kai Arras, ASL-EPFL
# adapted from v.1.2, 03.12.03, Kai Arras, CAS-KTH: (x,a,b) interface
import numpy as np
import matplotlib.pyplot as plt


def drawellipse(x, a, b, color):

    # Compose point vector with 100 ooint resolution
    ivec = np.linspace(0, 2*np.pi, 100)    # index vector
    p = np.matrix([])
    p = np.matrix([a*np.cos(ivec), b*np.sin(ivec)])    # hold ellipse points

    # Translate and rotate
    xo = x[0]
    yo = x[1]
    angle = x[2]
    R = np.matrix([[np.cos(angle), -np.sin(angle)],
                   [np.sin(angle), np.cos(angle)]])
    T = np.matrix([[xo], [yo]])*np.ones(len(ivec))
    p = R*p + T
    p = np.squeeze(np.array(p))

    # Plot
    h = plt.plot(p[0, :], p[1, :], color)
    return h
