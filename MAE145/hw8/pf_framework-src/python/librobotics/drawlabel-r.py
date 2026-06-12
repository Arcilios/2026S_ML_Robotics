#DRAWLABEL Draw scalable text.
#   DRAWLABEL(X,STR,SCALE,OFFSET,COLOR) draws scalable text STR at
#   pose X = [x y theta] imitating the OCR font. With SCALE = 1,
#   the height of the letters is 1 meter. OFFSET shifts the text in
#   [m] from the x,y position in positive x- and y-direction. COLOR
#   is either a [r g b]-vector or a color string such as 'r' or 'g'.
#
#   Currently, the following characters are implemented: 0,1,2,3,4,
#   5,6,7,8,9,W,R,S,E,F,M,P
#
#   H = DRAWLABEL(...) returns a column vector of handles to all
#   line objects of the drawing, one handle per line.
#
#   See also TEXT.
#
# v.1.0, 09.11.02, Kai Arras, ASL-EPFL
# v.1.1, Nov.2003, Kai Arras, CAS-KTH: minor modifications
import numpy as np
import matplotlib.pyplot as plt


def drawlabel(x, string, scale, offset, color):

    # Constants
    xsqueeze = 0.6           # scale x for non-square letters
    xkerning = 0.9           # distance between letters in x
    rx = 0.5                 # round-corner-factor
    ry = rx*xsqueeze         # account for squeeze in x
    # 1. Fill in point and lengths-vector
    n = len(string)
    xtmp = x[0]
    y = x[1]
    theta = x[2]
    x = xtmp
    points = []
    lengths = []
    for i in range(n):
        #switch string[i],
        if string[i] == '0':
            x_vec = [rx, 4-rx, 4, 4, 4-rx, rx, 0, 0, rx]
            y_vec = [0, 0, ry, 4-ry, 4, 4, 4-ry, ry, 0]
        elif string[i] == '1':
            x_vec = [0, 4, 4, 4, 2, 2, 0]
            y_vec = [0, 0, 1, 0, 0, 4, 4]
        elif string[i] == '2':
            x_vec = [4, 0, 0, rx, 4-rx, 4, 4, 4-rx, 0]
            y_vec = [0, 0, 2-ry, 2, 2, 2+ry, 4-ry, 4, 4]
        elif string[i] == '3':
            x_vec = [0, 4-rx, 4, 4, 4-rx, 1, 4-rx, 4, 4, 4-rx, 0]
            y_vec = [0, 0, ry, 2-ry, 2, 2, 2, 2+ry, 4-ry, 4, 4]
        elif string[i] == '4':
            x_vec = [3, 3, 3, 4, 0, 0]
            y_vec = [0, 3, 1.5, 1.5, 1.5, 4]
        elif string[i] == '5':
            x_vec = [0, rx, 4-rx, 4, 4, 4-rx, 1, 1, 4]
            y_vec = [ry, 0, 0, ry, 2-ry, 2, 2, 4, 4]
        elif string[i] == '6':
            x_vec = [1, 0, 0, rx, 4-rx, 4, 4, 4-rx, 0]
            y_vec = [4, 4, ry, 0, 0, ry, 1.7-ry, 1.7, 1.7]
        elif string[i] == '7':
            x_vec = [2, 2, 4, 4, 0, 0]
            y_vec = [0, 1.7, 3, 4, 4, 3.6]
        elif string[i] == '8':
            x_vec = [rx, 0, 0, rx, 4-rx, 4, 4, 4-rx,
                     rx, 1, 1, 1+rx, 3-rx, 3, 3]
            y_vec = [2, 2-ry, ry, 0, 0, ry, 2-ry, 2, 2, 2, 4-ry, 4, 4, 4-ry, 2]
        elif string[i] == '9':
            x_vec = [3, 4, 4, 4-rx, rx, 0, 0, rx, 4]
            y_vec = [0, 0, 4-ry, 4, 4, 4-ry, 2.3+ry, 2.3, 2.3]
        elif string[i] == 'W':
            x_vec = [0, 0, rx, 2-rx, 2, 2, 2, 2+rx, 4-rx, 4, 4]
            y_vec = [4, 2*ry, 0, 0, ry, 2.8, ry, 0, 0, 2*ry, 4]
        elif string[i] == 'R':
            x_vec = [0, 0, 4-rx, 4, 4, 4-rx, 0, 0.5, 4]
            y_vec = [0, 4, 4, 4-ry, 2.5+ry, 2.5, 2.5, 2.5, 0]
        elif string[i] == 'S':
            x_vec = [0, 0, rx, 4-rx, 4, 4, 0, 0, rx, 4-rx, 4, 4]
            y_vec = [0.7, ry, 0, 0, ry, 0.7, 3.3, 4-ry, 4, 4, 4-ry, 3.3]
        elif string[i] == 'E':
            x_vec = [4, 0, 0, 2.3, 0, 0, 4]
            y_vec = [0, 0, 2, 2, 2, 4, 4]
        elif string[i] == 'F':
            x_vec = [0, 0, 2.3, 0, 0, 4]
            y_vec = [0, 2.5, 2.5, 2.5, 4, 4]
        elif string[i] == 'M':
            x_vec = [0, 0, 0.5, 2, 2, 2, 3.5, 4, 4]
            y_vec = [0, 4, 4, 2.8, 2.5, 2.8, 4, 4, 0]
        elif string[i] == 'P':
            x_vec = [0, 0, 4-rx, 4, 4, 4-rx, 0]
            y_vec = [0, 4, 4, 4-ry, 1.8+ry, 1.8, 1.8]
        else:
            print(['drawlabel: Warning: Letter "',
                   string[i], '" not implemented'])
                
        x_vec = np.array(x_vec)   
        y_vec = np.array(y_vec)
        x_vec = x_vec + 4*offset/(scale*xsqueeze)
        y_vec = y_vec + 4*offset/scale
        if not points is True:
            # holds all points
            points = np.matrix([x_vec*xsqueeze+xkerning*(i)/4, y_vec/4])
            # holds the number of points of each letter
            lengths = [len(x_vec)] 
        else:
            # for the cases we have above, it should not enter here; 
            # the following block has not been fixed
            # '/4': normalize to 1 'i' letter kerning
            points = np.matrix(points)
            shp = points.shape
            points = np.matrix([[points[0, 0:shp[1]+1], 
                                 x_vec/4*xsqueeze+xkerning*(i)],
                                 [points[1, 0:shp[1]+1], y_vec/4]])
            lengths = [lengths, len(x_vec)]
            
    # 2. Scale, translate and rotate
    R = np.matrix([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])   
    midlen = len(np.transpose(points))            
    T = np.matrix([[x], [y]])*np.ones((1, midlen))
    points = R*scale*points + T

    # 3. Plot letter-by-letter
    istart = 0
    h = []
    #fig = plt.figure(1)
    plt.figure(1)
    #ax = fig.suplot(1,1,1)
    spd = points.shape
    print(spd)
    for i in range(n):
        iend = istart + lengths[i] 
        #fig = plt.figure()
        #ax = fig.add_suplot(1,1,1)
        plt.plot(points[0, istart:iend+1],
                      points[1, istart:iend+1], color)
        istart = iend + 1
    #return fig_h, fig_hi
        #h = cat(1,h,hi)
    
