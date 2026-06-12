# Creates a generic list of elements
# *args: a sequence of integers (element in the list, and list organization)
# Examples:
#  ndlist(0,k) : a list of k elements (with zero as an element of the list)
#  ndlist(0,k,m) : a list with k sublists having m (zero) elements each
#        ndlist(0,2,5) = [[0,0,0,0,0], [0,0,0,0,0]]
#  ndlist(0,k,m,s) : a list with k sublists, each k sublist has m sublists,
#        the m sublists have s (0) elements
#        ndlist(0,2,2,5) = [[[0,0,0,0,0], [0,0,0,0,0]],
#                           [[0,0,0,0,0],[0,0,0,0,0]]]
import copy


def ndlist(init, *args):  # python 2 doesn't have kwarg after *args
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in range(x)]  # Python 2 xrange
    return dp
