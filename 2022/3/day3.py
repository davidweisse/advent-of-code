with open("input/day3_input.txt") as f:
    input = f.read().split()

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
for i in range(len(input)):
    for item in input[i][:len(input[i]) // 2]:
        if item in input[i][len(input[i]) // 2:]:
            sum += alph.index(item) + 1
            break

print("Sol1:", sum)

sum = 0
for i in range(0, len(input), 3):
    for item in input[i]:
        if item in input[i + 1] and item in input[i + 2]:
            sum += alph.index(item) + 1
            break

print("Sol2:", sum)