#DIFFANGLE Take difference of two angles and unwrap it.
#   A = DIFFANGLE(A1,A2) determines the minimal difference
#   A = A1-A2 between two angles A1 and A2. If either A1 or A2
#   is Inf, Inf is returned.

#   See also NORMANGLE.

# v.1.0, Dec. 2017, S. Martinez adapted from Kai Arras', CAS-KTH


import numpy as np
import math
from normalangle import normalangle

def diffangle(a1,a2):
    if a1 < math.inf and a2 < math.inf:

        # normalize angles a1 and a2
        a1 = normalangle(a1,0)
        a2 = normalangle(a2,0)

        # Take the difference and unwrap
        delta = a1 - a2
        if a1 > a2:
            while delta > np.pi:
                delta = delta - 2*np.pi
        elif a2 > a1:
            while delta < - np.pi:
                delta = delta + 2*np.pi
    else:
        delta = math.inf
         
    return delta

  
 
