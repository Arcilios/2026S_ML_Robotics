# A17370336

def computeLineThroughTwoPoints(p1, p2):
    # Extract the coordinates of the two input points.
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    # Compute the direction vector of the line from p1 to p2.
    ux = x2 - x1
    uy = y2 - y1
    # A normal vector to (ux, uy) is (-uy, ux).
    # a(x2​−x1​)+b(y2​−y1​)=0
    a = -uy
    b = ux
    # Normalize (a, b) 
    norm = (a * a + b * b) ** 0.5
    a = a / norm
    b = b / norm
    # Solve for c by substituting point p1 into ax + by + c = 0.
    c = -(a * x1 + b * y1)
    return a, b, c

def computeDistancePointToLine(q, p1, p2):
    # Compute the normalized line coefficients.
    a, b, c = computeLineThroughTwoPoints(p1, p2)
    # Since (a, b) is normalized, |ax + by + c| is the distance
    distance = abs(a * q[0] + b * q[1] + c)
    return distance

def computeDistancePointToSegment(q, p1, p2):
    # Extract coordinates of the segment endpoints and query point.
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    xq, yq = q[0], q[1]
    # u is the segment direction vector from p1 to p2.
    ux = x2 - x1
    uy = y2 - y1
    # v is the vector from p1 to q.
    vx = xq - x1
    vy = yq - y1
    # Compute the squared length of the segment.
    segment_len_square = ux * ux + uy * uy
    # Compute the projection parameter t of q onto the line.
    # t < 0 means the closest point is before p1,
    # t > 1 means the closest point is after p2,
    # 0 <= t <= 1 means the closest point lies on the segment.
    t = (vx * ux + vy * uy) / segment_len_square
    if t <= 0:
        # Closest point is p1.
        distance = ((xq - x1) ** 2 + (yq - y1) ** 2) ** 0.5
        w = 1
    elif t >= 1:
        # Closest point is p2.
        distance = ((xq - x2) ** 2 + (yq - y2) ** 2) ** 0.5
        w = 2
    else:
        # Closest point is the orthogonal projection on the segment
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