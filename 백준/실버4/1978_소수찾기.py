def check(num):
    if num > 2:
        for i in range(2, num):
            if num % i:
                continue
            else:
                return 0
        return 1
    elif num == 2:
        return 1
    else:
        return 0

n = int(input())
nums = list(map(int, input().split()))
answer = 0
for num in nums:
    answer += check(num)
print(answer)
