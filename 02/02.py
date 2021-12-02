
with open('02.txt') as f:
    lines = [x.split(" ") for x in f.readlines()]
    vert = horiz = aim = 0
    for command, amount in lines:
        amount = int(amount)
        if command == 'forward':
            horiz = horiz + amount
            vert = vert + aim * amount
        elif command == 'down':
            aim = aim + amount
        else:
            aim = aim - amount
    print(horiz * vert)
