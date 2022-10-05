from itertools import combinations

candidates = []
for _ in range(9):
    candidates.append(int(input()))

combis = combinations(candidates, 7)

for combi in combis:
    if sum(combi) == 100:
        for i in combi:
            print(i)