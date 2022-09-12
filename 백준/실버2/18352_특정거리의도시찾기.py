from collections import deque

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    index, target = map(int, input().split())
    cities[index].append(target)
# answer = [[0] for _ in range(n+1)]

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(start)
    visited[start] = x
    while queue:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            for next in cities[now]:
                # 아직 방문 안 한 곳이라면
                if visited[next] == 0:
                    visited[next] = visited[now] + 1
                    queue.append(next)
    flag = 1
    for i in range(1, m+1):
        if visited[i] == k+1:
            print(i)
            flag = 0
    if flag:
        print(-1)

bfs(x)

