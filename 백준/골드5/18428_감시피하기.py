def overlook_possibility( tr, tc):
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for di in direction:
        nr, nc = tr + di[0], tc + di[1]
        while 0 <= nr < n and 0 <= nc < n and hallway[nr][nc] != 'O':
            if hallway[nr][nc] == 'S':
                return True
            else:
                nr += di[0]
                nc += di[1]
    return False

def put_obstacles(turns):
    global answer
    # 세 번 설치했으면
    if turns == 3:
        cnt = 0
        for r in range(n):
            for c in range(n):
                if hallway[r][c] == 'T':
                    if not overlook_possibility(r, c):
                        cnt += 1
        if cnt == teacher_cnt:
            answer = 'YES'
        return

    for r in range(n):
        for c in range(n):
            if hallway[r][c] == 'X':
                hallway[r][c] = 'O'
                turns += 1
                put_obstacles(turns)
                hallway[r][c] = 'X'
                turns -= 1


n = int(input())
hallway = [list(input().split()) for _ in range(n)]
teacher_cnt = 0
answer = 'NO'
for i in range(n):
    for j in range(n):
        if hallway[i][j] == 'T':
            teacher_cnt += 1


put_obstacles(0)
print(answer)