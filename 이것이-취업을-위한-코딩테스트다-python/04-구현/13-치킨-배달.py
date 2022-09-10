from itertools import combinations

n, m = map(int, input().split())
# 위쪽과 왼쪽에 패딩
city = [[0]*n]
for _ in range(n):
    temp = list(map(int, input().split()))
    temp = [0] + temp
    city.append(temp)

# 집의 좌표와 치킨집 좌표 미리 체크
homes = []
chickens = []
for r in range(1, n+1):
    for c in range(1, n+1):
        if city[r][c] == 1:
            # 집이면 homes에 담아두기
            homes.append([r, c])
        elif city[r][c] == 2:
            # 치킨집이면 chickens에 담아두기
            chickens.append([r, c])

# 거리의 최장 합은 최악의 경우(모두 끝에서 끝까지 가는 경우)
min_distance = 200 * len(homes)

# 모든 경우를 순회해보자
for i in range(1, m+1):
    # 치킨집 고르는 경우의 수
    cases = list(combinations(chickens, i))
    # 각 경우에서의 거리 확인하기
    for case in cases:
        # print('********new case*************')
        # print(case) # i개 만큼의 치킨집만 남겼을 때
        sum_distance = 0
        for home in homes:
            temp_distance = 200  # 한 집당 최대 거리
            # print(f'home: {home}')
            # 골라둔 치킨집과의 거리 구하기
            for chicken in case:
                # print(chicken)
                # 현 상황에서 구한 거리
                now_distance = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
                # print(now_distance)
                # 이전에 확인한 치킨집과 거리 비교해서 더 짧은 거리 선택
                if temp_distance > now_distance:
                    temp_distance = now_distance
            # print(temp_distance)
            # 반복해서 제일 짧은 거리만 더하기
            sum_distance += temp_distance
            # print('--------chicken---------')
        if min_distance > sum_distance:
            min_distance = sum_distance
print(min_distance)
