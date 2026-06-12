# Reads the odometry and sensor readings from a file,
# in this case filename = "sensor_data.text".
# (Adaptation from read_data in octave)
#
# filename: path to the file to parse between quotes
# data: structure containing the parse information
#
# The data is returned in a nested list where u_t and z_t are stored
# in item t-1 of the outer list, with t-1 starting at 0.
# A z_t  can contain observations of multiple
# landmarks.
#
# Usage:
# - access the readings for timestep t (with t >= 1)
#   data[t-1]
#   this returns a list containing the odometry reading and all
#   landmark observations, which can be accessed as follows
# - odometry reading at timestep t:
#   data[t-1][0]
# - sensor reading at timestep t:
#   data[t-1][1:]
#
# Odometry readings have the following fields:
# - r1 : rotation 1
# - t  : translation
# - r2 : rotation 2
# which correspond to the identically labeled variables in the motion mode.
#
# Sensor readings can again be indexed and each of the entries have the
# following fields:
# - id      : id of the observed landmark
# - range   : measured range to the landmark
# - bearing : measured angle to the landmark (you can ignore this)
#
# Examples:
# - Translational component of the odometry reading at timestep 10
#   data[9][0][1]
# - Measured range to the second landmark observed at timestep 4
#   data[3][2][1]
from ndlist import ndlist


def read_data(filename):
    with open(filename, "r") as f:
        words = f.readlines()
    lng = len(words)
    for i in range(lng):
        words[i] = words[i].split(' ')
        words[i][3] = words[i][3][:-1]
        for j in range(1, 4):
            words[i][j] = float(words[i][j])
    data = words
    timestep = 0
    # the first measurement corresponds to entry 0
    for t in range(lng):
        if words[t][0] == 'ODOMETRY':
            timestep = timestep + 1

    odom = ndlist(0, timestep, 4)
    u = 0
    for t in range(lng):
        if words[t][0] == 'ODOMETRY':
            odom[u][0] = u + 1
            odom[u][1:4] = words[t][1:4]
            u = u + 1

    v = lng - timestep
    sensor = ndlist(0, v, 4)
    time = 1
    u = 0
    for t in range(lng):
        if words[t][0] == 'SENSOR' and t < lng - 1:
            sensor[u][0] = time
            sensor[u][1:4] = words[t][1:4]
            u = u + 1
            if words[t+1][0] == 'ODOMETRY':
                time = time + 1
        elif t == lng-1:
            sensor[u][0] = time
            sensor[u][1:4] = words[t][1:4]

    data = []
    for t in range(len(odom)):
        temp = [odom[t][1:]]
        for u in range(len(sensor)):
            if sensor[u][0] == t + 1:
                sensor[u][1] = int(sensor[u][1])
                temp.insert(sensor[u][1], sensor[u][1:])
        data.insert(t, temp)

    return data
