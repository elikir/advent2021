import pprint


def get_covered_points(start, end):
    covered_points = []
    
    x1 = start[0]
    x2 = end[0]

    y1 = start[1]
    y2 = end[1]
    
    horiz = True
    static = 0

    # it's a vertical line
    if x1 == x2:
        static = x1
        horiz = False
        # it's backwards
        if y2 < y1:
            start_point = y2
            end_point = y1
        else:
            start_point = y1
            end_point = y2

    # it's a horizontal line
    elif y1 == y2:
        static = y1
        # it's backwards
        if x2 < x1:
            start_point = x2
            end_point = x1
        else:
            start_point = x1
            end_point = x2
    for x in range(start_point, end_point + 1):
        if not horiz:
            posn = (static, x)
        else:
            posn = (x, static)
        covered_points.append(posn)
    return covered_points



with open('01.txt') as f:
    lines = [x.split("->") for x in f.readlines()]
    point_pairs = []
    for line in lines:
        start = [int(x) for x in line[0].split(",")]
        end = [int(x) for x in line[1].split(",")]
        point_pairs.append((start, end))
    points = {}
    for pair in point_pairs:
        for point in get_covered_points(pair[0], pair[1]):
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    count = 0
    for point, amt in points.items():
        if amt >= 2:
            count += 1
    print(count)
