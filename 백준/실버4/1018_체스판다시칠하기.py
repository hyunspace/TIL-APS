from pprint import pprint

def coloring(sr, sc):
    global answer
    this_cnt = 0
    white_cnt = 0
    black_cnt = 0
    smallboard = []
    white = 'WBWBWBWB'
    black = 'BWBWBWBW'
    for i in range(sr, sr+8):
        rows = ''
        for j in range(sc, sc+8):
            rows += bigboard[i][j]
        smallboard.append(rows)
    # pprint(smallboard)

    # 흰색 기준으로 한 번 세고
    for k in range(8):
        if k % 2 == 0:
            for d in range(8):
                if smallboard[k][d] != white[d]:
                    white_cnt += 1
        else:
            for d in range(8):
                if smallboard[k][d] != black[d]:
                    white_cnt += 1

    # 검정 기준으로 한 번 세기
    for k in range(8):
        if k % 2 == 0:
            for d in range(8):
                if smallboard[k][d] != black[d]:
                    black_cnt += 1
        else:
            for d in range(8):
                if smallboard[k][d] != white[d]:
                    black_cnt += 1
    if white_cnt >= black_cnt:
        this_cnt = black_cnt
    else:
        this_cnt = white_cnt

    if answer > this_cnt:
        answer = this_cnt


n, m = map(int, input().split())
bigboard = [list(input()) for _ in range(n)]
# print(bigboard)

answer = n*m

for r in range(n):
    if r + 7 < n:
        for c in range(m):
            if c + 7 < m:
                coloring(r, c)

print(answer)