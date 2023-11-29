with open("day10_input.txt") as input:
    l = [int(d) for d in input.read().split()]

l.sort()
print(l)
diff = [0, 0, 0]
diffs = [1]
for i in range(1, len(l)):
    difference = l[i]-l[i-1]
    diffs.append(difference)
diffs.append(3)
for i in diffs:
    diff[i-1] += 1

arrs = 0

print(diffs)
print(diff)
print(diff[0]*diff[2])