# 961
# def st(n):
#     print("~!@#$^&*()_+|")
#
# n = int(input())
# for _ in range(n):
#     st(n)


# 962
# def circle(r):
#     print(f'{r ** 2 * 3.14:.2f}')
#
# circle(int(input()))


# 963
# def square(n):
#     start = 1
#     for _ in range(n):
#         for _ in range(n):
#             print(start, end=' ')
#             start += 1
#         print()
# square(int(input()))


# 964
# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     elif c >= a and c >= b:
#         return c
#
# a, b, c = map(int, input().split())
# print(find_max(a, b, c))


# 965
# def return_squared(m, n):
#     ans = m
#     if n == 0:
#         return print(1)
#     for _ in range(n-1):
#         ans *= m
#     return print(ans)
# m, n = map(int, input().split())
# return_squared(m, n)


# 966
# def calculate(lst):
#     if lst[1] == '+':
#         return print(f'{lst[0]} + {lst[2]} = {int(lst[0]) + int(lst[2])}')
#     elif lst[1] == '-':
#         return print(f'{lst[0]} - {lst[2]} = {int(lst[0]) - int(lst[2])}')
#     elif lst[1] == '*':
#         return print(f'{lst[0]} * {lst[2]} = {int(lst[0]) * int(lst[2])}')
#     elif lst[1] == '/':
#         return print(f'{lst[0]} / {lst[2]} = {int(lst[0]) // int(lst[2])}')
#     else:
#         return print(0)
# lst = list(input().split())
# calculate(lst)


# 967
# def ans(a, b):
#     if a > b:
#         a //= 2
#         b *= 2
#         return print(a, b)
#     else:
#         a *= 2
#         b //= 2
#         return print(a, b)
# a, b = map(int, input().split())
# ans(a, b)


# 968
# def gugudan(a, b):
#     if a < b:
#         pass
#     else:
#         a, b = b, a
#     for i in range(a, b+1):
#         print(f'== {i}dan ==')
#         for j in range(1, 10):
#             print(f'{i} * {j} = {str(i*j).rjust(2)}')
#         print()
#     return
# a, b = map(int, input().split())
# gugudan(a, b)


# 969
# def at():
#     return print('@'*10)
#
# print('first')
# at()
# print('second')
# at()
# print('third')
# at()


# 970
# def total(n):
#     ans = n
#     for i in range(1, n):
#         ans += i
#     return print(ans)
#
# total(int(input()))


# 971
# def square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             print(i*j, end=' ')
#         print()
#     return
# square(int(input()))


# 972
# def minus(a, b):
#     if a > b:
#         return print(a**2 - b**2)
#     else:
#         return print(b**2 - a**2)
# a, b = map(int, input().split())
# minus(a, b)


# 973
# def total(arr):
#     for student in arr:
#         print(*student, sum(student))
#     allsum = 0
#     for j in range(3):
#         subject = 0
#         for i in range(3):
#             subject += arr[i][j]
#         print(subject, end=' ')
#         allsum += subject
#     print(allsum)
#
# scores = []
# for _ in range(3):
#     scores.append(list(map(int, input().split())))
#
# total(scores)