# 221001 시간초과!

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

answer = 1
cases = []
while True:
    cnt = 0
    for line in lines:
        cnt += line // answer
    if cnt == n:
        cases.append(answer)
    answer += 1
    if cnt < n:
        break
print(max(cases))
