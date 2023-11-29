with open("day7_input.txt") as input:
    l = [int(d) for d in input.read().split(",")]

best_pos = 0
min_fuel = 9E999999
for i in range(1, max(l)+1):
    fuel = 0
    print(str(int(i/max(l)*100)) + '%', i)
    for j in l:
        for k in range(1, abs(j-i)+1):
            fuel += k
    if fuel < min_fuel:
        min_fuel = fuel
        best_pos = i

print(best_pos, min_fuel)