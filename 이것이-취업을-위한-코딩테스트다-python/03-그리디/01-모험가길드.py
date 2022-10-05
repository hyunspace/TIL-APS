from collections import deque
N = int(input())
advs = deque()
advs = list(map(int, input().split()))
# 공포도가 작은 사람들 먼저 묶어서 세기
advs.sort()
cnt = 0
groups = []
while advs:
    if advs[0] > len(advs):
        break
    else:
        group = advs[0:advs[0]]
        if len(group) >= max(group):
            cnt += 1
            advs = advs[advs[0]:]
        else:
            break
print(cnt)

