
with open('01.txt') as f:
    lines = [x.split(' ') for x in f.readlines()]
    horiz = vert = 0
    for direction, amount in lines:
        amount = int(amount)
        if direction == 'forward':
            horiz = horiz + amount
        elif direction == 'down':
            vert = vert + amount
        else:
            vert = vert - amount

    print(vert * horiz)
    

