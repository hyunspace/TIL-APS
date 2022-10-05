n, m = map(int, input().split())
first = [list(map(int, input().split())) for _ in range(n)]
second = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        first[i][j] += second[i][j]
for i in range(n):
    print(*first[i])