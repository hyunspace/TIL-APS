n, k = map(int, input().split())

result1 = result2 = 1
for _ in range(k):
    result1 *= n
    n -= 1
for _ in range(k-1):
    result2 *= k
    k -= 1

print(result1//result2)