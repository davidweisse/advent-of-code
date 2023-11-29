with open("input/day2_input.txt") as f:
    input = f.read().split()

l = list()
d = {
    'A': 0, 'X': 0,
    'B': 1, 'Y': 1,
    'C': 2, 'Z': 2
}

for x in input:
    l.append(d.get(x))

score = 0
for i in range(0, len(l), 2):
    score += l[i + 1] + 1
    if (l[i] + 1) % 3 == l[i + 1]:
        score += 6
    elif l[i] == l[i + 1]:
        score += 3

print("Sol1:", score)

score = 0
for i in range(0, len(l), 2):
    if l[i + 1] == 0:
        score += ((l[i] - 1) % 3) + 1
    elif l[i + 1] == 1:
        score += l[i] + 4
    else:
        score += ((l[i] + 1) % 3) + 7

print("Sol2:", score)