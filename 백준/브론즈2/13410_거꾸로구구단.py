n, m = map(int, input().split())
nums = []
for i in range(1, m + 1):
    temp = n * i
    num = 0
    for j in range(len(temp) - 1, -1, -1):
        num += temp % (10 ** j)
    temp.append(num)
print(max(temp))

