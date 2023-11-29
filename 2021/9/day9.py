with open("day9_input.txt") as input:
    l = input.read().split()
    for i in range(len(l)):
        l[i] = [int(d) for d in l[i]]

low_points = []
for i in range(len(l)):
    for j in range(len(l[i])):
        neighbors = []
        if i > 0:
            neighbors.append(l[i-1][j])
        if i < len(l)-1:
            neighbors.append(l[i+1][j])
        if j > 0:
            neighbors.append(l[i][j-1])
        if j < len(l[i])-1:
            neighbors.append(l[i][j+1])
        lowest = True
        for n in neighbors:
            if l[i][j] >= n:
                lowest = False
        if lowest:
            low_points.append([i, j])
        #print(l[i][j], neighbors, lowest)

print(low_points)

def rec(i, j, visited):
    #print(pos, visited)
    if i >= 0 and i < len(l) and j >= 0 and j < len(l[0]):
        if [i, j] not in visited:
            if l[i][j] != 9:
                visited.append([i, j])
                rec(i-1, j, visited)
                rec(i+1, j, visited)
                rec(i, j-1, visited)
                rec(i, j+1, visited)

lengths = []
for i, j in low_points:
    visited = []
    rec(i, j, visited)
    lengths.append(len(visited))

lengths.sort()
print(lengths)

sum = 0
for i, j in low_points:
    sum += l[i][j]+1

print(sum)