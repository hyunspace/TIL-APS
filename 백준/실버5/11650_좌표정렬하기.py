import sys
input = sys.stdin.readline

n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]
coordinates.sort()
for i in range(n):
    a, b = coordinates[i]
    print(a, b)