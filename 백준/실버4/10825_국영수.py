import sys
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    name, korean, eng, math = input().split()
    korean, eng, math = map(int, [korean, eng, math])
    scores.append([name, korean, eng, math])
scores.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])