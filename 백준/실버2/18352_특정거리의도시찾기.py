from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    index, target = map(int, input().split())
    cities[index].append(target)
distance = [0] * (n+1)

def bfs(start):
    answer = []
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for next in cities[now]:
            # 아직 방문 안 한 곳이라면
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
                distance[next] = distance[now] + 1
                if distance[next] == k:
                    answer.append(next)
    if len(answer) > 0:
        answer.sort()
        for city in answer:
            print(city)
    else:
        print(-1)
    # flag = 1
    # for i in range(1, n+1):
    #     if visited[i] == k+1:
    #         print(i)
    #         flag = 0
    # if flag:
    #     print(-1)

bfs(x)

