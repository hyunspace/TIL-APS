from itertools import combinations
N = int(input())
coins = list(map(int, input().split()))
# 동전들의 합이 가장 크게 만들 수 있는 양의 정수 금액
# 총 합에 해당하는 정수는 무조건 만들 수 있으므로 굳이 확인할 필요 X
check = [0] * (sum(coins))
# 모든 경우의 수(부분 집합)
for i in range(len(coins)):
    sub_sets = list(combinations(coins, i))
    for sub_set in sub_sets:
        check[sum(sub_set)] += 1
print(check.index(0))