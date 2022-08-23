n, m = map(int, input().split())
cr, cc, di = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]
direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
answer = 1
turn_cnt = 0
while turn_cnt < 4:
    game_map[cr][cc] = 2
    dr, dc = cr + direction[di][0], cc + direction[di][1]
    if 0 <= dr < n and 0 <= dc < m and game_map[dr][dc] == 0:
        game_map[dr][dc] = 2
        answer += 1
        cr, cc = dr, dc
        di = (di + 1) % 4
        turn_cnt = 0
    else:
        di -= 1
        if di == -1:
            di = 3
        turn_cnt += 1
print(answer)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1