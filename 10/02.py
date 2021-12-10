
scores = {')':1, ']':2,'}':3,'>':4}

match = {'{':'}','(':')','[':']', '<':'>'}

def autocomplete(line):
    stack = []
    for char in line:
        if char in match:
            stack.append(match[char])
        else:
            if stack.pop() != char:
                return None
    to_return = stack.copy()
    return to_return[::-1]



with open('01.txt') as f:
    ff = [x[:-1] for x in f.readlines()]
    score_list = [] 
    for line in ff:
        total = 0
        score = autocomplete(line)
        if score:
            for char in score:
                total *= 5
                total += scores[char]
            score_list.append(total)
    print(list(sorted(score_list))[int(len(score_list)/2)])
