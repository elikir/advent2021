
def one_or_zero(amt, total, reverse=False):
    if not reverse:
        return '1' if amt > total / 2 else '0'
    return '0' if amt > total / 2 else '1'

with open('01.txt') as f:
    ff = f.readlines()
    ff = [[int(y) for y in x[:-1]] for x in ff]
    linesm = [[ff[j][i] for j in range(len(ff))] for i in range(len(ff[0]))]
    ones = [sum(x) for x in linesm]
    gamma = ''.join([one_or_zero(x, len(ff)) for x in ones])
    epsilon = ''.join([one_or_zero(x, len(ff), True) for x in ones])

print(int(gamma,2) * int(epsilon,2))
