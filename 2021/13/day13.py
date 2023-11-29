with open("day13_input.txt") as input:
    l, instructions = input.read().split("\n\n")
    l = [s.split(",") for s in l.split()]
    for i in range(len(l)):
        l[i] = [int(d) for d in l[i]]
    instructions = instructions.split("\n")
    for i in range(len(instructions)):
        instructions[i] = [instructions[i][instructions[i].index("=")-1], int(instructions[i][instructions[i].index("=")+1:])]

max_x = 0
max_y = 0
for x, y in l:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

print(max_x, 'x', max_y)

paper = [['.' for i in range(max_x+1)] for i in range(max_y+1)]
def draw(arr):
    for i in arr:
        s = ""
        for j in i:
            s += j
        print(s)
for e in l:
    paper[e[1]][e[0]] = '#'
#draw(paper)
#print(instructions)

for dir, pos in instructions:
    print("fold", dir, pos)
    l_fold = []
    if dir == 'y':
        l_fold = paper[pos+1:]
        paper = paper[:pos]
        #print(len(paper), len(l_fold))
        for y_paper, y_fold in zip(range(len(paper)-1, -1, -1), range(len(l_fold))):
            #print(y_paper, y_fold)
            for i in range(len(paper[y_paper])):
                if l_fold[y_fold][i] == '#':
                    paper[y_paper][i] = '#'
    if dir == 'x':
        l_fold = [s[pos+1:] for s in paper]
        paper = [s[:pos] for s in paper]
        for x_paper, x_fold in zip(range(len(paper[0])-1, -1, -1), range(len(l_fold[0]))):
            for i in range(len(paper)):
                if l_fold[i][x_fold] == '#':
                    paper[i][x_paper] = '#'
    #draw(paper)

draw(paper)
counter = 0
for i in paper:
    for j in i:
        if j == '#':
            counter += 1
print(counter)