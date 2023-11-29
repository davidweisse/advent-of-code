with open("input/day5_input.txt") as f:
    input = f.read().split("\n\n")

stacks = [[], [], [], [], [], [], [], [], []]
currstack = 0
i = 0
while i < len(input[0]):
    if input[0][i] == ' ':
        i += 3
        currstack += 1
    elif input[0][i] == '[':
        stacks[currstack].insert(0, input[0][i + 1])
        currstack += 1
        i += 3
    if i < len(input[0]) and input[0][i] == '\n':
        currstack = 0
    i += 1

instr = input[1].split("\n")

instr = [x.split() for x in instr]
instr = [[int(x[1]), int(x[3]), int(x[5])] for x in instr]

stacks2 = list()
for i in stacks:
    stacks2.append(list(i))


for i in instr:
    for j in range(i[0]):
        e = stacks2[i[1] - 1].pop()
        stacks2[i[2] - 1].append(e)
    
s = ""
for stack in stacks2:
    s += stack[-1]
print("Sol1:", s)

for i in instr:
    a = list()
    for j in range(i[0]):
        e = stacks[i[1] - 1].pop()
        a.append(e)
    for j in range(i[0]):
        e = a.pop()
        stacks[i[2] - 1].append(e)

s = ""
for stack in stacks:
    s += stack[-1]
print("Sol2:", s)