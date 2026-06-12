#DRAWRECT Draw rounded rectangle.
#   DRAWRECT(X,W,H,R,FILLED,COLOR) draws a rectangle with
#   round corners of radius R, width W and height H, centered at
#  pose X where X is the 1x3 vector [x, y, theta]. With FILLED = 1
#   the rectangle is filled with color COLOR, with FILLED = 0
#   only the contour is drawn. COLOR is a [r g b]-vector or a
#   Matlab color string such as 'r' or 'g'.
#   Note that 2R must be greater or equal than the smaller of the
#   two values W,H. For 2R = W = H, DRAWRECT draws a circle.
#   H = DRAWRECT(...) returns the graphic handle H.
#   See also DRAWREFERENCE, PLOT.
#    Sonia M. adapted from Kai Arras', CAS-KTH "

import numpy as np
import matplotlib.pyplot as plt


def drawrect(x, w, h, r, filled, color):
    # Constants
    # RESO = np.pi/18   # angular resolution of arc primitive
    # Prepare vectors and transform matrices
    arc = np.linspace(0, np.pi/2, 10)
    n = len(arc)
    vec = np.ones(n)
    T = np.array([x[0], x[1]])
    T.shape = (2, 1)
    R = np.matrix([[np.cos(x[2]), -np.sin(x[2])],
                  [np.sin(x[2]), np.cos(x[2])]])
    # Compute and concatenate contour points
    p = np.ones(2*n)
    p.shape = (2, n)
    p[0, :] = r*np.cos(arc)
    p[1, :] = r*np.sin(arc)
    p1 = p + np.matrix([[w/2-r], [h/2-r]])*vec
    p2 = np.matrix([[0, 1], [-1, 0]])*p + np.matrix([[w/2-r], [-h/2+r]])*vec
    p3 = np.matrix([[-1, 0], [0, -1]])*p + np.matrix([[-w/2+r], [-h/2+r]])*vec
    p4 = np.matrix([[0, -1], [1,  0]])*p + np.matrix([[-w/2+r], [h/2-r]])*vec
    p = np.ones(2*4*n)
    p.shape = (2, 4*n)
    p[:, 0:n] = p1
    p[:, n:2*n] = p4
    p[:, 2*n:3*n] = p3
    p[:, 3*n:4*n] = p2
    p[0, 4*n-1] = p[0, 0]
    p[0:3, 4*n-1] = p[0:3, 0]   # close contour
    # Transform points to pose x
    p = R*p + T*np.ones(4*n)
    a = np.array(p[0, :])
    a.shape = 4*n
    b = np.array(p[1, :])
    b.shape = 4*n
    # Draw
    if filled == 1:
        h = plt.fill(a, b, color)
    else:
        h = plt.plot(a, b, color)

    return h
