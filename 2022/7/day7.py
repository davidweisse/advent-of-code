with open("input/day7_input.txt") as f:
    input = f.read().splitlines()

stack, sizes = list(), list()

for line in input:
    if line == "$ cd ..":
        size = stack.pop()
        sizes.append(size)
        stack[-1] += size
    elif line[:5] == "$ cd ":
        stack.append(0)
    elif line[0].isdigit():
        stack[-1] += int(line.split()[0])

print(stack)

while stack:
    size = stack.pop()
    sizes.append(size)
    if stack:
        stack[-1] += size

print(sum(s for s in sizes if s <= 100000))
print(min(s for s in sizes if s >= sizes[-1] - 40000000))