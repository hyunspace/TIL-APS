# 22년 10월 10일
# n = int(input())
# nums = []
# nums.extend(map(int, input().split()))
#
# for i in range(1, min(nums)+1):
#     cnt = 0
#     for j in nums:
#         if j % i == 0:
#             cnt += 1
#     if cnt == len(nums):
#         print(i)


# 10월 15일
import sys
input = sys.stdin.readline

def gcd(a, b):
    # if a < b:
    #     a, b = b, a
    print(a, b)
    if b == 0:
        return a
    else:
        print(a, b)
        return gcd(b, a%b)

# def gcd(a, b):
#     print(a, b)
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)
gcd(16, 6)
print('-'*12)
gcd(6,16)

# n = int(input())
# nums = list(map(int, input().split()))
# common_divider = gcd(nums[0], gcd(nums[1], nums[-1])) # 최대 3개임 ㅠㅠ
# for i in range(1, common_divider//2 + 1):
#     if common_divider % i == 0:
#         print(i)
# print(common_divider)
