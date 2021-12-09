from collections import Counter

# this is ugly, but used to show the math behind it
sum_dict = {
    1: 8+9,
    2: 8+8+7+4+7,
    3: 8+8+7+9+7,
    4: 6+7+8+9,
    5: 6+8+7+9+7,
    6: 8+6+7+4+7+9,
    7: 8+8+9,
    8: 8+6+8+7+4+9+7,
    9: 8+6+7+8+9+7,
    0: 8+8+9+7+4+6
    }

def take_two(inp, out):
    temp_dict = {}
    char_dict = Counter(''.join(inp))
    for digit in inp:
        score = sum([char_dict[x] for x in digit])
        temp_dict[digit] = score
    return_str = ''

    # this could be flipped in the dict, but I wanted to prove a point with my logic
    key_list = list(sum_dict.keys())
    val_list = list(sum_dict.values())
    for dig in out:
        score = sum([char_dict[x] for x in dig])
        actual = key_list[val_list.index(score)]
        return_str += str(actual)
    return int(return_str)

with open('01.txt') as f:
    lines = f.read().split("\n")[:-1]

    values = []
    for line in lines:
        inp, outp = line.split("|")
        inp = list(filter(lambda x: x, inp.split(" ")))
        outp = list(filter(lambda x: x, outp.split(" ")))
        values.append((inp, outp))

    print(sum([take_two(x[0], x[1]) for x in values]))
