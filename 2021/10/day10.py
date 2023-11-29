with open("day10_input.txt") as input:
    l = input.read().split()

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
brackets = "()[]{}<>"

incomplete = []

sum = 0
for row in l:
    prev = []
    corrupted = False
    for c in row:
        if c in opening:
            prev.append(c)
        elif c in closing:
            if brackets[brackets.index(c)-1] == prev[-1]:
                prev.pop()
            else:
                corrupted = True
                if c == ')':
                    sum += 3
                elif c == ']':
                    sum += 57
                elif c == '}':
                    sum += 1197
                elif c == '>':
                    sum += 25137
                break
    if not corrupted:
        incomplete.append(row)

scores = []
print(incomplete)
for row in incomplete:
    prev = []
    for c in row:
        if c in opening:
            prev.append(c)
        elif c in closing:
            prev.pop()
    s = ""
    for i in range(len(prev)-1, -1, -1):
        s += brackets[brackets.index(prev[i])+1]
    score = 0
    for c in s:
        score *= 5
        if c == ')':
            score += 1
        elif c == ']':
            score += 2
        elif c == '}':
            score += 3
        elif c == '>':
            score += 4
    scores.append(score)

print(sum)
scores.sort()
print(scores)
print(scores[len(scores)//2])