#  DRAWROBOT Draw robot.
#   DRAWROBOT(X,COLOR) draws a robot at pose X = [x y theta] such
#   that the robot reference frame is attached to the center of
#   the wheelbase with the x-axis looking forward. COLOR is a
#   [r g b]-vector or a color string such as 'r' or 'g'.
#
#   DRAWROBOT(X,COLOR,TYPE) draws a robot of type TYPE. Five
#   different models are implemented:
#      TYPE = 0 draws only a cross with orientation theta
#      TYPE = 1 is a differential drive robot without contour
#      TYPE = 2 is a differential drive robot with round shape
#      TYPE = 3 is a round shaped robot with a line at theta
#      TYPE = 4 is a differential drive robot with rectangular shape
#      TYPE = 5 is a rectangular shaped robot with a line at theta
#
#   DRAWROBOT(X,COLOR,TYPE,W,L) draws a robot of type TYPE with
#   width W and length L in [m].
#
#   H = DRAWROBOT(...) returns a column vector of handles to all
#   graphic objects of the robot drawing. Remember that not all
#   graphic properties apply to all types of graphic objects. Use
#   FINDOBJ to find and access the individual objects.
#
#   See also DRAWRECT, DRAWARROW, FINDOBJ, PLOT.
#
#   v.1.0, 16.06.03, Kai Arras, ASL-EPFL
#   v.1.1, 12.10.03, Kai Arras, ASL-EPFL: uses drawrect
#   adapted from v.1.2, 03.12.03, Kai Arras, CAS-KTH : types implemented"

import numpy as np
import matplotlib.pyplot as plt
from drawrect import drawrect
from drawarrow import drawarrow
from drawellipse import drawellipse
from inspect import signature


def drawrobot(x, color, *args):
    # Constants
    DEFT = 2            # default robot type
    DEFB = 0.4          # default robot width in [m], defines y-dir. of {R}
    WT = 0.03           # wheel thickness in [m]
    DEFL = DEFB+0.2     # default robot length in [m]
    WD = 0.2            # wheel diameter in [m]
    RR = WT/2           # wheel roundness radius in [m]
    RRR = 0.04          # roundness radius for rectangular robots in [m]
    HL = 0.09           # arrow head length in [m]
    CS = 0.1            # cross size in [m], showing the {R} origin

    # input argument check
    inputerr = 0
    sig = signature(drawrobot)
    lon = len(sig.parameters)
    params = np.array(args)

    if lon == 2:
        xvec = x
        color = color
        robottype = DEFT
        B = DEFB
        L = DEFL
    elif lon == 3:
        xvec = x
        color = color
        robottype = params[0]
        B = DEFB
        L = DEFL
    elif lon == 5:
        xvec = x
        color = color
        robottype = args[0]
        B = args[1]
        L = args[2]
    else:
        inputerr = 1

    '# Main statement'

    if inputerr == 0:
        x = xvec[0]
        y = xvec[1]
        theta = xvec[2]
        T = np.array([x, y])
        T.shape = (2, 1)
        R = np.matrix([[np.cos(theta), - np.sin(theta)],
                       [np.sin(theta), np.cos(theta)]])

        if robottype == 0:
            # Draw origin cross
            v = np.matrix([[CS, -CS, 0, 0], [0, 0, -CS, CS]])
            p = R*v + T*np.ones(4)   # horiz. line
            p = np.squeeze(np.array(p))
            h = plt.plot(p[0, 0:2], p[1, 0:2], color,
                         p[0, 2:5], p[1, 2:5], color)
        elif robottype == 1:
            # Draw wheel pair with axis and arrow
            xlw = np.array([x + B/2*np.cos(theta + np.pi/2),
                            y + B/2*np.sin(theta + np.pi/2), theta])
            # left wheel, call the function drawrect
            h1 = drawrect(xlw, WD, WT, RR, 1, color)
            xlw = np.array([x - B/2*np.cos(theta + np.pi/2),
                            y - B/2*np.sin(theta + np.pi/2), theta])
            # right wheel, call the function drawrect
            h2 = drawrect(xlw, WD, WT, RR, 1, color)

            # Draw axis cross with arrow
            v = np.matrix([[0, 0], [-B/2 + WT/2, B/2 - WT/2]])
            p = R*v + T*np.ones(2)
            p = np.squeeze(np.array(p))
            h3 = plt.plot(p[0, :], p[1, :], color)
            v = np.array([L/2, 0])
            v.shape = (2, 1)
            p = R*v + T
            # call the function drawarrow
            p = np.squeeze(np.array(p))
            h4 = drawarrow(T, p, 1, HL, color)
            h = [h1, h2, h3, h4]

        elif robottype == 2:
            # Draw wheel pair with axis and arrow
            xlw = np.array([x + B/2*np.cos(theta + np.pi/2),
                            y + B/2*np.sin(theta + np.pi/2), theta])
            # left wheel, call the function drawrect
            h1 = drawrect(xlw, WD, WT, RR, 1, color)
            xlw = np.array([x - B/2*np.cos(theta + np.pi/2),
                            y - B/2*np.sin(theta + np.pi/2), theta])
            # right wheel, call the function drawrect
            h2 = drawrect(xlw, WD, WT, RR, 1, color)

            # Draw axis cross with arrow
            v = np.matrix([[0, 0], [-B/2 + WT/2, B/2 - WT/2]])
            p = R*v + T*np.ones(2)
            p = np.squeeze(np.array(p))
            h3 = plt.plot(p[0, :], p[1, :], color)
            v = np.array([(B + WT)/2, 0])
            v.shape = (2, 1)
            p = R*v + T
            p = np.squeeze(np.array(p))
            h4 = drawarrow(T, p, 1, HL, color)

            # Draw circular contour
            radius = (B + WT)/2
            h5 = drawellipse(xvec, radius, radius, color)
            h = [h1, h2, h3, h4, h5]

        elif robottype == 3:
            # Draw circular contour
            radius = (B+WT)/2
            h1 = drawellipse(xvec, radius, radius, color)
          
            # Draw line with orientation theta with length radius
            v = np.array([(B+WT)/2, 0])
            v.shape = (2, 1)
            p = R*v + T
            p = np.squeeze(np.array(p))
            h2 = plt.plot([T[0], p[0]], [T[1], p[1]], color)
            h = [h1, h2]

        elif robottype == 4:
            # Draw wheel pair with axis and arrow
            xlw = np.array([x + B/2*np.cos(theta + np.pi/2),
                            y + B/2*np.sin(theta + np.pi/2), theta])
            # left wheel, call the function drawrect
            h1 = drawrect(xlw, WD, WT, RR, 1, color)
            xlw = np.array([x - B/2*np.cos(theta+np.pi/2),
                            y - B/2*np.sin(theta+np.pi/2), theta])

            # right wheel, call the function drawrect
            h2 = drawrect(xlw, WD, WT, RR, 1, color)

            # Draw axis cross with arrow
            v = np.matrix([[0, 0], [-B/2 + WT/2, B/2 - WT/2]])
            p = R*v + T*np.ones(2)
            p = np.squeeze(np.array(p))
            h3 = plt.plot(p[0, :], p[1, :], color)
            v = np.array([(B + WT)/2, 0])
            v.shape = (2, 1)
            p = R*v + T
            p = np.squeeze(np.array(p))
            h4 = drawarrow(T, p, 1, HL, color)

            # Draw rectangular contour
            h5 = drawrect(xvec, L, B, RRR, 0, color)
            h = [h1, h2, h3, h4, h5]

        elif robottype == 5:
            # Draw rectangular contour
            h1 = drawrect(xvec, L, B, RRR, 0, color)
            # Draw line with orientation theta with length L
            v = np.array([L/2, 0])
            v.shape = (2, 1)
            p = R*v + T
            h2 = plt.plot([T[0], p[0]], [T[1], p[1]], color)
            h = [h1, h2]

        else:
            print('drawrobot: Unsupported robot type')
            h = []
    elif inputerr == 1:
        print('wrong number of input arguments')
        h = []

    return h
