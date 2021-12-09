
# kind of a two-fer.  if it's a low, return risk, otherwise 0
def is_basin(x, y, heightmap):
    above, below, left, right = 10, 10, 10, 10
    #print(x, y, len(heightmap[y]), len(heightmap))    
    if y > 0:
        above = heightmap[y-1][x]
    if y <= len(heightmap) - 2:
        below = heightmap[y+1][x]
    if x > 0:
        left = heightmap[y][x-1]
    if x <= len(heightmap[y]) - 2:
        right = heightmap[y][x+1]
    pos = heightmap[y][x]

    #print(pos, above, right, below, left)
    return pos < above and pos < below and pos < left and pos < right


def basin_size(x, y, heightmap, seen=set()):
    if heightmap[y][x] == 9 or (x, y) in seen:
        return
    seen.add((x, y))    
    if y > 0:
        basin_size(x, y-1, heightmap, seen)
    if y <= len(heightmap) - 2:
        basin_size(x, y+1, heightmap, seen)
    if x > 0:
        basin_size(x-1, y, heightmap, seen)
    if x <= len(heightmap[y]) - 2:
        basin_size(x+1, y, heightmap, seen)

    return len(seen)
with open('01.txt') as f:
    ff = f.readlines()
    heightmap = [[int(y) for y in list(x[:-1])] for x in ff]
    low_points = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if is_basin(x, y, heightmap):
                low_points.append((x, y))
    sizes = []
    for pt in low_points:
        sizes.append(basin_size(pt[0], pt[1], heightmap, set()))
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

