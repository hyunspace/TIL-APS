a, b = map(int, input().split())
if a < b:
    a, b = b, a

# 최대 공약수 구하기
c = a % b
answer = 0
for i in range(b, 1, -1):
    if b % i == 0 and c % i == 0:
        answer = i
        print(answer)
        break
if answer == 0:
    answer = 1
    print(answer)

# 최소 공배수 구하기
print((a*b) // answer)