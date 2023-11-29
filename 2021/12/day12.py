from collections import defaultdict

with open("day12_input.txt") as input:
    raw = [s.split("-") for s in input.read().split()]
    l = []
    for s in raw:
        i = -1
        for e in range(len(l)):
            if s[0] == l[e][0]:
                i = e
        if i == -1:
            l.append([s[0]])
            for j in range(len(l)):
                if s[0] in l[j]:
                    i == j
        if s[1] not in l[i] and s[1] != "start":
            l[i].append(s[1])
        i = -1
        for e in range(len(l)):
            if s[1] == l[e][0]:
                i = e
        if i == -1:
            l.append([s[1]])
            for j in range(len(l)):
                if s[1] in l[j]:
                    i == j
        if s[0] not in l[i] and s[0] != "start":
            l[i].append(s[0])

print(l)

ans = 0
visited = defaultdict(int)

def dfs(cave):
    global ans
    if cave == "end":
        ans += 1
        return
    if cave.islower():
        visited[cave] += 1
        more_than_once = 0
        for small in visited:
            more_than_once += visited[small] > 1
            if visited[small] > 2:
                visited[cave] -= 1
                return
        if more_than_once > 1:
            visited[cave] -= 1
            return

    index = 0
    for i in range(len(l)):
        if l[i][0] == cave:
            index = i
    for nbr in l[index][1:]:
        dfs(nbr)
    if cave.islower():
        visited[cave] -= 1

dfs("start")
print(ans)

"start,A,b,A,c,A,end"