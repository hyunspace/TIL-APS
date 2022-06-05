# a = [1,2,3]
# b = [2,4,6]
# c = [3,6,9]
#
# print(a+c+c+c+b)

# lst = [1, 2]
# lst.append(int(input()))
# print(*lst[::-1], sep='\n')


# num1, time1 = map(int, (input().split()))
# num2, time2 = map(int, (input().split()))
#
# lst = list(num1 for _ in range(time1))
# lst.extend(num2 for _ in range(time2))
# print(lst)


# numbers = list(input().split())
# ans = []
# for idx in range(len(numbers)):
#     if (idx+1) % 3 == 0:
#         ans.append(numbers[idx])
# print(ans)

lst = list(input().split())
print(lst[-2:0:-1])