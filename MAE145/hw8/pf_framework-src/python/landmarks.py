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
# landmark[4][1]


def realworld(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    lng = len(data)
    landmarks = []
    for j in range(lng):
        if j != 4:
            landmarks.append([float(data[j][0]),
                              float(data[j][2]), float(data[j][4])])
        else:
            landmarks.append([float(data[4][0]),
                              float(data[4][2:4]), float(data[4][5])])
    return landmarks
