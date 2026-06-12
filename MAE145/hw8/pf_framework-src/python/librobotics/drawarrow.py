#   DRAWARROW Draw an arrow head.
#   DRAWARROW(XS,XE,FILLED,HSIZE,COLOR) draws an arrow from XS to
#   XE. The first two elements of XS,XE are interpreted as the
#   x- and y-positions. FILLED enabled and disabled head filling,
#   HSIZE scales the size of the head in [m], and COLOR is a
#   [r g b]-vector or a color string including quotes s.t. 'r' or 'g'.
#
#   H = DRAWARROW(...) return a column vector of handles to the
#   graphic objects of the arrow drawing.
#
#   See also DRAWREFERENCE, PLOT.


#   adapted from v.1.1, 09.11.02, Kai Arras, ASL-EPFL

import matplotlib.pyplot as plt
import numpy as np
import math


def drawarrow(x1, x2, filled, hsize, color):
    # Constants
    headangle = np.pi/9   # default arrow head opening angle

    # Compute all 3 points: head center, left and right
    xs = x1[0]
    ys = x1[1]
    xe = x2[0]
    ye = x2[1]
    phi = math.atan2(ye-ys, xe-xs)
    xhl = xe + hsize*np.cos(phi+np.pi-headangle)
    yhl = ye + hsize*np.sin(phi+np.pi-headangle)
    xhr = xe + hsize*np.cos(phi+np.pi+headangle)
    yhr = ye + hsize*np.sin(phi+np.pi+headangle)
    # Plot arrow head using the fill command
    #fig = plt.figure()
    if filled == 1:
        xarrow = [xs, xe, xhl, xhr, xe, xs]
        yarrow = [ys, ye, yhl, yhr, ye, ys]
        plt.fill(xarrow, yarrow, color, ec = color)
    else:
        xarrow1 = [xs, xe, xhl]
        yarrow1 = [ys, ye, yhl]
        xarrow2 = [xhr, xe]
        yarrow2 = [yhr, ye]
        plt.plot(xarrow1, yarrow1, color, xarrow2, yarrow2, color)
    
