with open("input/day9_input.txt") as f:
    input = f.read().split()

visited = set()
x = y = xt = yt = 0
for i in range(0, len(input), 2):
    n = int(input[i + 1])
    if input[i] in ("D", "L"):
        n = -n
    for j in range(0, n, n // abs(n)):
        if input[i] in ("L", "R"):
            x += n // abs(n)
        else:
            y += n // abs(n)
        if abs(x - xt) > 1:
            yt = y
            xt += n // abs(n)
        elif abs(y - yt) > 1:
            xt = x
            yt += n // abs(n)
        visited.add((xt, yt))

print(len(visited))