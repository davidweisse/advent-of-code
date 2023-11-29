from collections import defaultdict

with open("day15_input.txt") as input:
    old_l = input.read().split()
    for i in range(len(old_l)):
        old_l[i] = [int(d) for d in old_l[i]]

#print(old_l)
l = []
for i in range(len(old_l)*5):
    element = []
    for j in range(len(old_l[0])*5):
        element.append((((old_l[i%len(old_l)][j%len(old_l[0])]+i//len(old_l)+j//len(old_l[0])) - 1) % 9) + 1)
    l.append(element)

#for s in l:
#   print(s)

max_x = len(l[0]) - 1
max_y = len(l) - 1

start = (0, 0)
end = (max_x, max_y)

queue = defaultdict(int)
for x in range(max_x+1):
    for y in range(max_y+1):
        queue[(x, y)] = -1
queue[start] = 0

def nbrs(pos):
    n = list()
    if pos[0] > 0: n.append((pos[0]-1, pos[1]))
    if pos[0] < max_x: n.append((pos[0]+1, pos[1]))
    if pos[1] > 0: n.append((pos[0], pos[1]-1))
    if pos[1] < max_y: n.append((pos[0], pos[1]+1))
    return n

counter = 0
while queue:
    if counter == 2:
        print(len(queue))
        counter = 0
    u = end
    for e in queue:
        #print(e, queue[e], u)
        if queue[e] != -1:
            if queue[u] == -1 or queue[e] < queue[u]:
                u = e
    if u == end:
        print(queue[end])
        break
    for v in nbrs(u):
        if v in queue:
            distance = queue[u] + l[v[1]][v[0]]
            if queue[v] == -1 or distance < queue[v]:
                queue[v] = distance
            #print(v, queue[v])
    queue.pop(u)
    #print(len(queue))

    counter += 1