test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

count = 0
with open('02.txt') as f:
    lines = [int(x) for x in f.readlines()]
    prev_sum = sum(lines[0:3])
    for x in range(3, len(lines)+1):
        window_start = x-3
        window_end = x
        cur_sum = sum(lines[window_start:window_end])
        if cur_sum > prev_sum:
            count = count + 1
        prev_sum = cur_sum

print(count)
