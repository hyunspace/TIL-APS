# 981
# def print_nums(arr):
#     arr.sort(reverse=True)
#     print(*arr)
#
# n = int(input())
# numbers = list(map(int, input().split()))
# print_nums(numbers)


# 982
# def existed(dates):
#     if dates[0] in [1, 3, 5, 7, 8, 10, 12] and 1 <= dates[1] <= 31:
#         return print('OK!')
#     elif dates[0] in [4, 6, 9, 11] and 1 <= dates[1] <= 30:
#         return print('OK!')
#     elif dates[0] == 2 and 1 <= dates[1] <= 28:
#         return print('OK!')
#     else:
#         return print('BAD!')
# dates = list(map(int, input().split()))
# existed(dates)


# 983
# def larger_int(nums):
#     if abs(nums[0]) > abs(nums[1]):
#         print(nums[0])
#     else:
#         print(nums[1])
#
# def smaller_flt(nums):
#     if abs(nums[0]) < abs(nums[1]):
#         print(nums[0])
#     else:
#         print(nums[1])
#
# ints = list(map(int, input().split()))
# floats = list(map(float, input().split()))
# larger_int(ints)
# smaller_flt(floats)


# 984
# def find_r(area):
#     return print(f'{(area/3.14)**(1/2):.2f}')
#
# area = int(input())
# find_r(area)


# 985
# import math
# floats = list(map(float, input().split()))
# decimal_points = [0, 1]
# ans = [0, 0, 0]
# for i in range(3):
#     flag = 1
#     points = floats[i] - floats[i] // 1
#     # 가장 큰 수
#     if decimal_points[0] < points:
#         decimal_points[0] = points
#         ans[0] = math.ceil(floats[i])
#         flag = 0
#     # 가장 작은 수 버림
#     if decimal_points[1] > points:
#         decimal_points[1] = points
#         ans[1] = math.floor(floats[i])
#         flag = 0
#     if flag:
#         ans[2] = round(floats[i])
# print(*ans)


# 985 (22-06-23 재도전)
# import math
# def func985():
#     numbers = list(map(float, input().split()))
#     data = {}
#     for idx in range(3):
#         data[idx] = abs(numbers[idx]) - abs(numbers[idx]) // 1
#     sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)
#     # print(sorted_data)
#     # for i in sorted_data:
#     #     print(i)
#     print(math.ceil(numbers[sorted_data[0][0]]), end=' ')
#     print(math.floor(numbers[sorted_data[2][0]]), end=' ')
#     print(round(numbers[sorted_data[1][0]]))
# func985()


# 985 (22-06-23 재도전2)
# import math
# numbers = list(map(float, input().split()))
# max_data = {}
# min_data = {}
# for index in range(3):
#     max_data[index] = math.ceil(numbers[index]) - numbers[index]
#     min_data[index] = numbers[index] - math.floor(numbers[index])
# print(max_data)
# print(min_data)


# 986
# numbers = list(map(int, input().split()))
#
# for i in range(9, -1, -1):
#     for j in range(1, )
#     if numbers[i] < numbers[i+1]:
#         numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#     print(numbers)


# 986 (22-06-23 재도전)
# nums = list(map(int, input().split()))
# for i in range(9):
#     for j in range(0, 9-i):
#         if nums[j] < nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#     print(*nums)


# 987
# n = int(input())
# nums = list(map(int, input().split()))


# 989
# def abs_total(nums):
#     ans = 0
#     for num in nums:
#         ans += abs(num)
#     return print(ans)
# nums = map(int, input().split())
# abs_total(nums)


# 990
# def print_squared(n):
#     return print(2**n)
# n = int(input())
# print_squared(n)


# 991
# def totals(floats):
#     total = rounded_total = 0
#     for num in floats:
#         total += num
#         rounded_total += round(num)
#     print(round(total/3))
#     print(round(rounded_total/3))
# floats = list(map(float, input().split()))
# totals(floats)


# 992
# nums = list(map(int, input().split()))
# for _ in range(3):
#     for i in range(6):
#         for j in range(i, 6):
#             if i+j+1 <7 and nums[i+j] > nums[i+j+1]:
#                 nums[i+j], nums[i+j+1] = nums[i+j+1], nums[i+j]
# print(*nums)


# 987
# def bubble_sort():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     for i in range(N):
#         for j in range(N-i-1):
#             if nums[j] < nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     print(*nums)
# bubble_sort()


# 988
# a, b = map(float, input().split())
# if a > b:
#     a, b = b, a
# cnt = 0
# for _ in range(int(a**(1/2)), int(b**(1/2))):
#     cnt += 1
# print(cnt)


# 992
nums = list(map(int, input().split()))
