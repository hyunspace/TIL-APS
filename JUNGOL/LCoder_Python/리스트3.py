# 1번
# n = int(input())
# ans = []
#
# for i in range(1, n+1):
#     ans.append(i**2)
# print(ans)


# 2번
# cnt = [0] * 26
# chars = list(input().split())
#
# for char in chars:
#     cnt[ord(char)-65] += 1
# for idx in range(26):
#     if cnt[idx] > 0:
#         print(f'{chr(idx+65)} : {cnt[idx]}')


# 3번
# numbers = list(input().split())
# cnt = [0] * 10
# for number in numbers:
#     if len(number) == 1:
#         cnt[0] += 1
#     else:
#         cnt[int(number[0])] += 1
# for idx in range(10):
#     if cnt[idx] > 0:
#         print(f'{idx} : {cnt[idx]}')


# 3번 (2) - 실행시간은 짧고 사용 메모리는 큼
# numbers = list(map(int, input().split()))
# cnt = [0] * 10
# for number in numbers:
#     if 0 <= number < 10:
#         cnt[0] += 1
#     else:
#         cnt[number//10] += 1
# for idx in range(10):
#     if cnt[idx] > 0:
#         print(f'{idx} : {cnt[idx]}')


# 4번
# n = int(input())
# arr = [100, n]
# while arr[-1] > 0:
#     arr.append(arr[-2] - arr[-1])
# print(*arr)


# 5번
# arr = [[5,8,10,6,4],[11,20,1,13,2],[7,9,14,22,3]]
# for i in arr:
#     for j in i:
#         print(str(j).rjust(2), end='   ')
#     print()


# 6번
# first_arr = [list(map(int, input().split())) for _ in range(2)]
# second_arr = [list(map(int, input().split())) for _ in range(2)]
# print('first array\nsecond array')
# for i in range(2):
#     for j in range(4):
#         print(first_arr[i][j] * second_arr[i][j], end=' ')
#     print()


# 7번
# students = [list(map(int, input().split())) for _ in range(5)]
# cnt = 0
# for student in students:
#     if sum(student) / 4 >= 80:
#         print('pass')
#         cnt += 1
#     else:
#         print('fail')
# print(f'Successful : {cnt}')


# 8번
# arrays = [[1, 1, 1, 1, 1] for _ in range(5)]
# for row in range(1, 5):
#     for column in range(1, 5):
#         arrays[row][column] = arrays[row-1][column] + arrays[row][column-1]
# for arr in arrays:
#     print(*arr)


# 형성평가 #
# 1번
# n = int(input())
# lst = list('No.'+str(num) for num in range(1, n+1))
# print(lst)


# 2번
# size, num = map(int, input().split())
# lst = list(True if idx % num == 0 else False for idx in range(size))
# print(lst)


# 3번
# nums = list(map(int, input().split()))
# cnt = [0] * 7
# for num in nums:
#     cnt[num] += 1
# for idx in range(1, 7):
#     print(f'{idx} : {cnt[idx]}')


# 4번
# scores = list(map(int, input().split()))
# cnt = [0] * 11
# for score in scores:
#     cnt[score//10] += 1
# for idx in range(10, -1, -1):
#     if cnt[idx] > 0:
#         print(f'{idx*10} : {cnt[idx]} person')


# 5번
# a, b = map(int, input().split())
# lst = [a, b]
# while len(lst) < 10:
#     lst.append((lst[-2]+lst[-1])%10)
# print(*lst)


# 6번
# arrs = [[3, 5, 9],[2, 11, 5],[8, 30, 10],[22, 5, 1]]
# total = 0
# for arr in arrs:
#     print(*arr)
#     total += sum(arr)
# arrs.append(total)
# print(arrs[-1])

# 7번
# print('1class? 2class? 3class? 4class?', end=' ')
# for team in range(1, 5):
#     scores = list(map(int, input().split()))
#     print(f'{team}class : {sum(scores)}')


# 8번
# first = [1, 0, 1, 0, 1]
# arr = [[0] * 5 for _ in range(5)]
# arr[0] = first
# for i in range(1, 5):
#     for j in range(5):
#         if 0 <= j - 1 < 5 and 0 <= j + 1 < 5:
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
#         elif 0 <= j - 1 < 5:
#             arr[i][j] = arr[i-1][j-1]
#         elif 0 <= j + 1 < 5:
#             arr[i][j] = arr[i-1][j+1]
# for a in arr:
#     print(*a)


# 9번
# print('first array')
# first = [list(map(int, input().split())) for _ in range(2)]
# print('second array')
# second = [list(map(int, input().split())) for _ in range(2)]
# third = [[], []]
# for i in range(2):
#     for j in range(3):
#         third[i].append(first[i][j] * second[i][j])
# for arr in third:
#     print(*arr)



# 10번
# lst = [list(map(int, input().split())) for _ in range(4)]
# ans = [[], [], 0]
# for j in range(2):
#     temp = 0
#     for i in range(4):
#         if j == 0:
#             ans[0].append(sum(lst[i])//2)
#             ans[2] += sum(lst[i])
#         temp += lst[i][j]
#     ans[1].append(temp//4)
# ans[2] //= 8
# for arr in ans:
#     try:
#         print(*arr)
#     except:
#         print(arr)


# 11번
# size = int(input())
# pascal = [[1] for _ in range(size)]
# for i in range(1, size):
#     for j in range(1, i+1):
#         try:
#             pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
#         except:
#             pascal[i].append(pascal[i - 1][j - 1])
#
# for arr in pascal[::-1]:
#     print(*arr)


# 12번
# uppers = [list(input().split()) for _ in range(3)]
# for i in range(3):
#     for j in range(5):
#         print(chr(ord(uppers[i][j])+32), end=' ')
#     print()