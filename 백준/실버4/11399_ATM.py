n = int(input())
times = list(map(int, input().split()))
times.sort()
answer = 0
temp = 0
for i in range(n):
    temp += times[i]
    answer += temp
print(answer)
