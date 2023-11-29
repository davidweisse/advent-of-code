from collections import defaultdict
with open("day14_input.txt") as input:
    polymer = input.readline().strip()
    input.readline()
    rules = input.read().split("\n")
    rules = [s.split(" -> ") for s in rules]

freqs = defaultdict(int)
for i in range(len(polymer)-1):
    freqs[polymer[i:i+2]] += 1

for i in range(40):
    new_freqs = freqs.copy()
    for pair in freqs:
        for key, ele in rules:
            if pair == key:
                new_freqs[pair] -= freqs[pair]
                new_freqs[pair[0]+ele] += freqs[pair]
                new_freqs[ele+pair[1]] += freqs[pair]
                break
    freqs = new_freqs

count = defaultdict(int)
for pair in freqs:
    count[pair[0]] += freqs[pair]
    count[pair[1]] += freqs[pair]

count[polymer[0]] += 1
count[polymer[-1]] += 1

count_vals = [c // 2 for c in count.values()]

lowest = min(count_vals)
highest = max(count_vals)

print(highest-lowest)