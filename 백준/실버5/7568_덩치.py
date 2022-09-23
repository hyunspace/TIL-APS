n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
ranks = [0] * n

for i in range(n):
    k = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            k += 1
    ranks[i] = k + 1

print(*ranks)