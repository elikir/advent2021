

def do_shit(ff):
    ff = [[int(y) for y in x[:-1]] for x in ff]
    linesm = [[ff[j][i] for j in range(len(ff))] for i in range(len(ff[0]))]
    ones = [sum(x) for x in linesm]
    gamma = ([one_or_zero(x, len(ff)) for x in ones])
    epsilon = ([one_or_zero(x, len(ff), True) for x in ones])
    return gamma, epsilon


def one_or_zero(amt, total, reverse=False):
    if not reverse:
        return '1' if amt >= total / 2 else '0'
    return '0' if amt >= total / 2 else '1'

with open('01.txt') as f:
    ff = f.readlines()
    gamma, epsilon = do_shit(ff)
    cp1 = ff.copy()
    cp2 = ff.copy()
    
    digit = 0
    while len(cp1) != 1:
        for line in range(len(cp1)):
            if int(cp1[line][digit]) != int(gamma[digit]):
                cp1[line] = ''
        cp1 = list(filter(lambda x: x, cp1))
        gamma, epsilon = do_shit(cp1)
        digit += 1
    digit = 0
    while len(cp2) != 1:
        print(epsilon)
        for line in range(len(cp2)):
            if int(cp2[line][digit]) != int(epsilon[digit]):
                    cp2[line] = ''
        cp2 = list(filter(lambda x: x, cp2))
        gamma, epsilon = do_shit(cp2)
        digit += 1

    o2_rating = int(cp1[0], 2)
    co2_rating = int(cp2[0], 2)
    print(o2_rating * co2_rating)



