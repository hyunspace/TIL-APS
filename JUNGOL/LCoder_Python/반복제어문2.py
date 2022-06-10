# for num in range(1, 6):
#     for k in range(1, 6):
#         print(num+k, end = ' ')
#     print()

row, column = map(int, input().split())
ans = []

for r in range(1, row+1):
    lst = []
    for c in range(1, 5):
        lst.append(r*c)
    ans.append(lst)

for l in ans:
    print(*l, end=' ')
    print()