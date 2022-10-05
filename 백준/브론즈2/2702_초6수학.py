t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    max_num = 0 #최대공약수
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0 and max_num < i:
            max_num = i
    min_num = max_num * (a//max_num) * (b//max_num)
    print(min_num, max_num)