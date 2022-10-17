import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
second = n*m*2*256
answer = 0

# 전체 층 다 반복
for floor in range(257):
    break_time, build_time = 0, 0

    # 땅을 순회하면서 시간 재기
    for i in range(n):
        for j in range(m):
            # 현재 높이랑 목표 높이랑 비교
            if ground[i][j] > floor:
                break_time += (ground[i][j] - floor)
            else:
                build_time += floor - ground[i][j]
    if break_time + b >= build_time:
        total_time = break_time * 2 + build_time
        if second >= total_time:
            second = total_time
            answer = floor
print(second, answer)