# print(ord('A'))
#
# i = 65
# while i <= 90:
#     print(chr(i), end='')
#     i += 1

# n = int(input())
# for i in range(n, 0, -1):
#     print(('*'*i).rjust(n))

# N = int(input())
# num = 1
# char = 65
#
# for n in range(N, 0, -1):
#     for i in range(n):
#         print(num, end=' ')
#         num += 1
#     for j in range(N - n + 1):
#         print(chr(char), end=' ')
#         char += 1
#     print()

# print(ord('a'))
#
# n = int(input())
#
# for i in range(97, 123):
#     if (i - 96) % n == 0:
#         print(chr(i), end='')

# n = int(input())
#
# for i in range(n, 1, -1):
#     num = i * 2 - 1
#     print(('*'*num).center(n*2-1))
# for j in range(1, n+1):
#     num = j * 2 - 1
#     print(('*'*num).center(n*2-1))

# n = int(input())
#
# for i in range(1, n+1):
#     ans = ''
#     for j in range(1, i+1):
#         ans += str(j) + ' '
#     print(ans.rstrip().rjust(n*2-1))

# n = int(input())
# cord = 65
# num = 0
#
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(cord), end=' ')
#         cord += 1
#     for k in range(n-i):
#         print(num, end=' ')
#         num += 1
#     print()

# 8번
# n = int(input())
# number = 1
# for i in range(n):
#     ans = ' '*(i*2)
#     for j in range(n, i, -1):
#         ans += str(number) + ' '
#         number += 1
#     print(ans)

# 9번
# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print('#', end=' ')
#     print()
# for i in range(n-1, 0, -1):
#     ans = ''
#     for j in range(i):
#         ans += '#' + ' '
#     ans = ans.rstrip()
#     print(ans.rjust(n*2-1))


#10번
n = int(input())
num = -1

for i in range(n):
    for j in range(n):
        num = (num + 2) % 10
        print(num, end=' ')
    print()