#DRAWLABEL Draw scalable text.  DRAWLABEL(X,STR,SCALE,CLR)
#   draws scalable text STR starting at location x,y in  X = [x; y; theta]
#   with orientation theta in X
#   imitating the OCR (sans-serif) font.  SCALE is a number between
#   [0,1000] (points, <10 is tiny) CLR is either a in matplotlib such as 'r' or 'g'.

#   To do this, we just use the text() command from pyplot and the
#   text_rotation.py example

#   it returns an object of handles with the text

import matplotlib.pyplot as plt
import numpy as np


def drawlabel(X,s,scale,clr):
    
    txtlabel = plt.text(X[0],X[1],'s', rotation = X[2], family =
                   'sans-serif', fontsize = scale, color = 'clr')
    return txtlabel

