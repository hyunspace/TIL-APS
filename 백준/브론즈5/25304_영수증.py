x = int(input())
n = int(input())
receipts = [list(map(int, input().split())) for _ in range(n)]

recalculate = 0
for receipt in receipts:
    a, b = receipt
    recalculate += a * b

if x == recalculate:
    print('Yes')
else:
    print('No')