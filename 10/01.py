scores = {
        ')':3,
        ']':57,
        '}':1197,
        '>':25137
        }

match = {'{':'}','(':')','[':']', '<':'>'}

def score_of_line(line):
    stack = []
    for char in line:
        if char in match:
            stack.append(match[char])
        else:
            if stack.pop() != char:
                return scores[char]
    return 0

with open('01.txt') as f:
    ff = [x[:-1] for x in f.readlines()]
    
    print(sum([score_of_line(x) for x in ff]))
