with open("input/day8_input.txt") as f:
    input = f.read().split()
    input = [[int(x) for x in y] for y in input]

sum = len(input) * 2 + len(input[0]) * 2 - 4
for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        if max(input[i][0:j]) < input[i][j] or \
           max(input[i][j + 1:]) < input[i][j] or \
           max(input[k][j] for k in range(i)) < input[i][j] or \
           max(input[k][j] for k in range(i + 1, len(input))) < input[i][j]:
            sum += 1

print(sum)

l = list()

for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        left = 0
        for c in range(j - 1, -1, -1):
            left += 1
            if input[i][c] >= input[i][j]:
                break
        right = 0
        for c in range(j + 1, len(input[0])):
            right += 1
            if input[i][c] >= input[i][j]:
                break
        top = 0
        for c in range(i - 1, -1, -1):
            top += 1
            if input[c][j] >= input[i][j]:
                break
        bottom = 0
        for c in range(i + 1, len(input)):
            bottom += 1
            if input[c][j] >= input[i][j]:
                break
        l.append(left * right * top * bottom)

print(max(l))