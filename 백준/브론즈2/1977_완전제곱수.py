m = int(input())
n = int(input())
answer = []
for i in range(m, n+1):
    root = i ** (1/2)
    if root == int(root):
        answer.append(i)
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)