# A17370336

def computeLineThroughTwoPoints(p1, p2):
    # Extract coordinates of the two given points p1 = (x1, y1), p2 = (x2, y2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    # The direction vector of the line is u = (x2 - x1, y2 - y1)
    ux = x2 - x1
    uy = y2 - y1

    # A line ax + by + c = 0 must have (a, b) perpendicular to direction vector u
    # Therefore, choose a normal vector n = (-uy, ux)
    # because dot(u, n) = (ux)(-uy) + (uy)(ux) = 0
    a = -uy
    b = ux

    # Normalize (a, b) so that sqrt(a^2 + b^2) = 1
    # This allows the distance formula |ax + by + c| to directly give Euclidean distance
    norm = (a * a + b * b) ** 0.5
    a = a / norm
    b = b / norm

    # Solve for c using point p1:
    # since p1 lies on the line → a*x1 + b*y1 + c = 0
    # so c = -(a*x1 + b*y1)
    c = -(a * x1 + b * y1)

    return a, b, c


def computeDistancePointToLine(q, p1, p2):
    # Compute normalized line coefficients (a, b, c)
    a, b, c = computeLineThroughTwoPoints(p1, p2)

    # Since (a, b) is normalized, the perpendicular distance from q to the line is:
    # distance = |a*xq + b*yq + c|
    distance = abs(a * q[0] + b * q[1] + c)

    return distance


def computeDistancePointToSegment(q, p1, p2):
    # Extract coordinates
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    xq, yq = q[0], q[1]

    # u = direction vector of segment p1 -> p2
    ux = x2 - x1
    uy = y2 - y1

    # v = vector from p1 to query point q
    vx = xq - x1
    vy = yq - y1

    # Squared length of the segment ||u||^2
    segment_len_square = ux * ux + uy * uy

    # Projection parameter:
    # t = (v · u) / (u · u)
    # This gives the position of projection of q onto the infinite line
    t = (vx * ux + vy * uy) / segment_len_square

    # Case 1: projection lies before p1 → closest point is p1
    if t <= 0:
        distance = ((xq - x1) ** 2 + (yq - y1) ** 2) ** 0.5
        w = 1

    # Case 2: projection lies after p2 → closest point is p2
    elif t >= 1:
        distance = ((xq - x2) ** 2 + (yq - y2) ** 2) ** 0.5
        w = 2

    # Case 3: projection lies on the segment
    else:
        # Distance is perpendicular distance to the line
        distance = computeDistancePointToLine(q, p1, p2)
        w = 0

    return distance, w


if __name__ == '__main__':
    q = [3, 4]
    p1 = [1, 1]
    p2 = [2, 2]
    a, b, c = computeLineThroughTwoPoints(p1, p2)
    distance_line = computeDistancePointToLine(q, p1, p2)
    distance_segment, w = computeDistancePointToSegment(q, p1, p2)
    print("Test 1")
    print("computeLineThroughTwoPoints:", a, b, c)
    print("computeDistancePointToLine:", distance_line)
    print("computeDistancePointToSegment:", distance_segment, w)

    q = [1, 2]
    p1 = [3, 2]
    p2 = [2, 2]
    a, b, c = computeLineThroughTwoPoints(p1, p2)
    distance_line = computeDistancePointToLine(q, p1, p2)
    distance_segment, w = computeDistancePointToSegment(q, p1, p2)
    print("Test 2")
    print("computeLineThroughTwoPoints:", a, b, c)
    print("computeDistancePointToLine:", distance_line)
    print("computeDistancePointToSegment:", distance_segment, w)

    q = [5, 1]
    p1 = [0, 2]
    p2 = [2, 2]
    a, b, c = computeLineThroughTwoPoints(p1, p2)
    distance_line = computeDistancePointToLine(q, p1, p2)
    distance_segment, w = computeDistancePointToSegment(q, p1, p2)
    print("Test 3")
    print("computeLineThroughTwoPoints:", a, b, c)
    print("computeDistancePointToLine:", distance_line)
    print("computeDistancePointToSegment:", distance_segment, w)

## Test Results
# Test 1
# computeLineThroughTwoPoints: -0.7071067811865475 0.7071067811865475 -0.0
# computeDistancePointToLine: 0.7071067811865475
# computeDistancePointToSegment: 2.23606797749979 2
# Test 2
# computeLineThroughTwoPoints: 0.0 -1.0 2.0
# computeDistancePointToLine: 0.0
# computeDistancePointToSegment: 1.0 2
# Test 3
# computeLineThroughTwoPoints: 0.0 1.0 -2.0
# computeDistancePointToLine: 1.0
# computeDistancePointToSegment: 3.1622776601683795 2