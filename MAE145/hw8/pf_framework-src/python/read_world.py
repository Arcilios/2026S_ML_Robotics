# Reads the world definition and returns a list of landmarks
# in our case filename = "world.text"
#
# filename: path of the file to load
# landmarks: list containing the parsed information
#
# Each landmark contains the following information
# - id: id of the landmark
# - x : x coordinate
# - y : y coordinate
# this is given in float values
#
# Examples:
# - Obtain x-coordinate of the 5-th landmark
# landmark[4][0]


def realworld(filename):
    with open(filename,"r") as f:
        data = f.readlines()
    l = len(data)
    words = range(l)
    i = 0
    for line in data:
        words[i] = line.split()
        for k in range(len(words[i])):
            words[i][k] = float(words[i][k])
        i = i + 1
    landmarks = words
    return landmarks
        
    
    
    
