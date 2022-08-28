from pprint import pprint

# 보드 정보
n = int(input())
board = [[0]*n for _ in range(n)]

# 사과 정보
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
for apple in apples:
    board[apple[0]][apple[1]] = 1

# 방향 변환 정보
l = int(input())
turns = []
for _ in range(l):
    sec, direction = input().split()
    turns.append([int(sec), direction])

# 동0서1남2북3 / 0왼 1오
di = [
    [[-1, 0, 3], [1, 0, 2]],
    [[1, 0, 2], [-1, 0, 3]],
    [[0, 1, 0], [0, -1, 1]],
    [[0, -1, 1], [0, 1, 0]]
]
answer = 0
toward = 0

def find_direction(next):
    global toward
    # next: 왼/오
    if next == 'L':
        return di[toward][0]
    else:
        return di[toward][1]

def dummy():
    global answer
    d = [0, 1]
    row, col = 0, 0
    trow, tcol = 0, 0
    for turn in turns:
        # 이동 시간동안
        for _ in range(turn[0] - answer):
            # 지금 자리 체크
            board[row][col] = 2
            flag = 1
            # 다음 좌표
            nrow, ncol = row + d[0], col + d[1]
            if 0 <= nrow < n and 0 <= ncol < n: # 보드 안
                if board[nrow][ncol] == 2: # 내 몸이야
                    flag = 0
                else: # 사과거나 빈칸이라면
                    if board[nrow][ncol] == 0: # 빈칸이라면 꼬리 바꾸기
                        # 꼬리가 앞으로
                        board[trow][tcol] = 0
                        # 새 꼬리
                        trow, tcol = trow + d[0], tcol + d[1]
                    board[nrow][ncol] = 2  # 지금 자리 표시하고
                    row, col = nrow, ncol  # 위치 정리
            else: # 보드 밖
                flag = 0
            if flag:
                answer += 1
            else:
                return answer
            print(answer)
            pprint(board)

        # 방향 바꿀 시간
        d = find_direction(turn[1])

print(dummy())