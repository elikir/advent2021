


with open('01.txt') as f:
    lines = f.read().split("\n")[:-1]

    count = 0

    for line in lines:
        output = list(filter(lambda x: x, line.split("|")[1].split(" ")))
        print(output)
        count += len(list(filter(lambda x: len(x) in [2,3,4,7], output)))
    print(count)
