
# kind of a two-fer.  if it's a low, return risk, otherwise 0
def get_risk(x, y, heightmap):
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
    if pos < above and pos < below and pos < left and pos < right:
        return pos + 1
    return 0


with open('01.txt') as f:
    ff = f.readlines()
    heightmap = [[int(y) for y in list(x[:-1])] for x in ff]
    count = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            count += get_risk(x, y, heightmap)
    print(count)
