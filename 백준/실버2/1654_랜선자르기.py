# 221001 시간초과!

# import sys
# input = sys.stdin.readline
#
# k, n = map(int, input().split())
# lines = []
# for _ in range(k):
#     lines.append(int(input()))
#
# answer = 1
# cases = []
# while True:
#     cnt = 0
#     for line in lines:
#         cnt += line // answer
#     if cnt == n:
#         cases.append(answer)
#     answer += 1
#     if cnt < n:
#         break
# print(max(cases))


# 221011 나무자르기 => 이진탐색!
k, n = map(int, input().split())
lines = list(int(input()) for _ in range(k))
start = 0
end = max(lines)
answer = []

while start <= end:
    center = (start + end) // 2
    nums = 0
    for line in lines:
        nums += line // center
    if nums > n:
        start = center + 1
    elif nums < n:
        end = center - 1
    else:
        break
print(center)