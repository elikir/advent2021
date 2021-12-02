count = 0
with open('01.txt') as f:
    prev_line = 9999999
    for line in f.readlines():
        line = int(line)
        if line > prev_line:
            count = count + 1
        prev_line = line

print(count)
