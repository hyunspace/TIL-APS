def find_path(row, column, score):
    global max_score

    # dfs로 탐색하자...!?

    # 방문 표시
    visited[row][column] = 1
    score += 1

    # 탐색 시작
    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for k in range(4):
        nr, nc = row + dr[k], column + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 8 and maps[row][column][1] < maps[nr][nc][1]:
            pass





T = int(input())

for tc in range(T):
    N = int(input())
    players = []
    for _ in range(N):3.
        mem, tree = input().split()
        players.append((mem, tree, 0))

    maps = [list(input().split()) for _ in range(5)]

    for idx in players:
        visited = [[0] * 8 for _ in range(5)]
        max_score = 0
        for r in range(5):
            for c in range(8):
                if maps[r][c][0] == players[idx][1]:
                    if maps[r][c][1] == 1: # 추가점수 얻고 시작
                        find_path(r, c, 1)
                    else:                  # 그냥 시작
                        find_path(r, c, 0)

    players.sort(key=lambda x:x[2])
    print(f'#{tc} {players[0][0]}')
