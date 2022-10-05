n, l = map(int, input().split())
label = 0
for i in range(n):
    while True:
        label += 1
        if not str(l) in str(label):
            break
    # print(i+1, label)
print(label)