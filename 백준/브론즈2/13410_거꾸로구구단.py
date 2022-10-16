n, m = map(int, input().split())
nums = []
for i in range(1, m + 1):
    temp = str(n * i)
    temp = temp[::-1]
    nums.append(int(temp))
print(max(nums))
