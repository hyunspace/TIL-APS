r, b = map(int, input().split())
total = r + b
temp_cases = []
cases = []

# 약수 조합 모두 찾기
for i in range(1, total+1):
    if total % i == 0:
        temp_cases.append([i, total // i])

# L > W을 고려하여 인덱스 0 값이 더 큰 약수 조합만 남기기
for index in range(len(temp_cases) // 2, len(temp_cases)):
    cases.append(temp_cases[index])

for case in cases:
    l, w = case
    check_r = l * 2 + (w - 2) * 2
    check_b = l * w - check_r
    if check_r == r and check_b == b:
        print(l, w)
        break
