import functools

@functools.lru_cache
def rec(days_left, age):
    if days_left == 0:
        return 1
    days_left -= 1
    if age == 0:
        return rec(days_left, 8) + rec(days_left, 6)
    else:
        return rec(days_left, age - 1)

with open('01.txt') as f:
    fishies = [int(x) for x in f.read().split(",")]
    DAYS = 256
    xx = sum([x for x in map(lambda x: rec(DAYS, x), fishies)])
    print(xx)
