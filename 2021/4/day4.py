with open("day4_input.txt") as input:
    numbers = [int(d) for d in input.readline().split(",")]
    l = [int(d) for d in input.read().split()]

boards = [[] for d in range(len(l)//25)]
for i in range(len(l)//25):
    for j in range(5):
        boards[i].append([d for d in l[i*25+j*5:i*25+j*5+5]])

def calculate_score(i, j):
    score = 0
    for r in boards[j]:
        for c in r:
            if c != 'x':
                score += c
    return score * numbers[i]

i = 0
winner = None
winners = 0
cache = []
while winners < len(boards):
    for j in range(len(boards)):
        for r in range(len(boards[j])):
            for c in range(len(boards[j][r])):
                if boards[j][r][c] == numbers[i]:
                    boards[j][r][c] = "x"
    for j in range(len(boards)):
        for r in range(len(boards[j])):
            if boards[j][r][0] == 'x' and boards[j][r][1] == 'x' and boards[j][r][2] == 'x' and boards[j][r][3] == 'x' and boards[j][r][4] == 'x':
                winner = j
                if winner not in cache:
                    winners += 1
                    cache.append(winner)
                    print(winner, boards[winner])
                    print(calculate_score(i, j))
            if boards[j][0][r] == 'x' and boards[j][1][r] == 'x' and boards[j][2][r] == 'x' and boards[j][3][r] == 'x' and boards[j][4][r] == 'x':
                winner = j
                if winner not in cache:
                    winners += 1
                    cache.append(winner)
                    print(winner, boards[winner])
                    print(calculate_score(i, j))
    i += 1
print(winners)
print("last board", calculate_score(i-1, winner))
print(cache)