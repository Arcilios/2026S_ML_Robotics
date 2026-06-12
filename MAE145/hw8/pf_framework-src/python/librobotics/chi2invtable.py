# This file shows how to compute  the inverse of the chi2 distribution
# using the modules scipy.stats.chi2 and the function stats.chi2.ppf

#  X = scipy.stats.chi2(p,v) just returns the inverse of the chi-square cumu-
#   lative distribution function (cdf) with v degrees of freedom at
#  the value p. The chi-square cdf with v degrees of freedom, is 
#   the gamma cdf with parameters V/2 and 2.   


#   At least, the function supports the degrees of freedom v between
#   1 and 100 and the probability levels p between 0 and 0.9999 

import scipy
from scipy import stats


def chi2_inverse(p,v):
    x = scipy.stats.chi2(p,v)
    return x
