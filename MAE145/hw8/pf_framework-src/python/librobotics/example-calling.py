#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 07:07:19 2017

@author: sonia

example passing plot handles to another file
this file : aims to plot what is in drawarrow
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from drawarrow import drawarrow
from drawrect import drawrect


def drawexample(drawarrow, x1, x2, x3, filled1, hsize, 
                color1, w, h, r, filled2, color2):
    drawarrow(x1[0:2], x2, filled1, hsize, color1)
    drawarrow(x1[0:2], x3, filled1, hsize, color1)
    drawrect(x1, w, h, r, filled2, color2)
      