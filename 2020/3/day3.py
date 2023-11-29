input = open("day3_input.txt")

l = input.read().split()

trees = 0
pos = 0
for i in range(len(l)):
    if l[i][pos] == '#':
        trees += 1
    pos = (pos + 3) % len(l[0])

print(trees)

pos = 0
width = len(l[0])
trees = 0
result = 1
for i in range(1, 9, 2):
    pos = 0
    trees = 0
    for j in range(len(l)-1):
        pos = (pos+i) % width
        if l[j+1][pos] == '#':
            trees += 1
    result *= trees
pos = 0
trees = 0
for i in range(0, len(l)-1, 2):
    pos = (pos+1) % width
    if l[i+2][pos] == '#':
            trees += 1
result *= trees    

print(result)
input.close()