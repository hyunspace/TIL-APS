n, k = map(int, input().split())
nums = list(range(1, n+1))
k -= 1
index = k
answer = []
for _ in range(n):
    # print(nums, index)
    if 0 <= index < len(nums):
        num = nums.pop(index)
        answer.append(num)
        # print(index, num)
        index += k
    else:
        index %= len(nums)
        num = nums.pop(index)
        answer.append(num)
        # print(index, num)
        index += k
    # print(nums)
    # print('----------')
print('<', end='')
for i in range(n):
    if i < n-1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end='>')