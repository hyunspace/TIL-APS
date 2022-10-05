from collections import deque

n, k = map(int, input().split())
examiner = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int, input().split())

def virus():
    queue = deque()
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for virus_num in range(k):
        queue.append(virus)
        for c in range(n):
            for r in range(n):
                for i in range(4):
                    nc = c + d[i][0]
                    nr = r + d[i][1]
                    if 0 <= nc < n and 0 <= nr < n and examiner[nc][nr] == 0:
                        examiner[nc][nr] = virus_num

for _ in range(s):
    virus()
    print(examiner)

print(examiner[target_x-1][target_y-1])
