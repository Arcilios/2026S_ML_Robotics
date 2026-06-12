#DRAWREFERENCE Draw coordinate reference frame.
#   DRAWREFERENCE(X,SIZE,COLOR) draws a reference frame at
#   pose X = [x;y;theta] 
#   SIZE is the length of the frame axes in [m], and COLOR is a
#   [r g b]-vector or a color string such as 'r' or 'g'.
#
#
#   See also DRAWARROW, DRAWLABEL, FINDOBJ, PLOT.
#
# adapted from v.1.0, 09.11.02, Kai Arras, ASL-EPFL
#
import numpy as np
from drawlabel import drawlabel
import matplotlib.pyplot as plt
from drawarrow import drawarrow


def drawreference(xvec, size, color):
    # Constants
    fill = 0                # enable/disable arrow head filling
    ahsize = size*0.2       # arrow head size
    fscale = size*0.15      # font size relative to the rest
    foffst = size*0.04      # font offset
    crsize = size*0.1       # cross size
    lh = size*0.55          # label offset from x-axis
    xk = 0.9                # default value XKERNING in drawlabel
    xs = 0.6                # default value XSQUEEZE in drawlabel
    fh = 2*foffst + fscale  # label frame height
    #
    x = xvec[0]
    y = xvec[1]
    phi = xvec[2]
    sphi = np.sin(phi)
    cphi = np.cos(phi)
    #
    # Draw cross
    px = np.array([x-crsize*cphi, x+crsize*cphi, x+crsize*sphi, x-crsize*sphi])
    py = np.array([y-crsize*sphi, y+crsize*sphi, y-crsize*cphi, y+crsize*cphi])
    plt.plot(px[0:2], py[0:2], color, px[2:5], py[2:5], color)

    # Plot x- and y-axis
    drawarrow(xvec, [x + size*cphi, y+size*sphi], fill, ahsize, color)
    drawarrow(xvec, [x - size*cphi, y+size*sphi], fill, ahsize, color)
    
