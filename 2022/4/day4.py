import re

with open("input/day4_input.txt") as f:
    input = f.read()

input = re.split(",|-|\n", input)
input = [int(x) for x in input]

count = 0
for i in range(0, len(input), 4):
    if input[i] <= input[i + 2] and input[i + 1] >= input[i + 3]:
        count += 1
    elif input[i] >= input[i + 2] and input[i + 1] <= input[i + 3]:
        count += 1

print(count)

count = 0
for i in range(0, len(input), 4):
    if input[i] <= input[i + 2] and input[i + 1] >= input[i + 2]:
        count += 1
    elif input[i + 2] <= input[i] and input[i + 3] >= input[i]:
        count += 1

print(count)