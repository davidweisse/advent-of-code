with open("input/day1_input.txt") as f:
    input = f.read().split("\n")
    input = [int(x) if x != "" else None for x in input]

sums = list()
current = 0

for x in input:
    if type(x) is int:
        current += x
    else:
        sums.append(current)
        current = 0

sums.sort(reverse=True)

print(sum(sums[:3]))