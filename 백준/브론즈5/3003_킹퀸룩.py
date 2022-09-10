whites = list(map(int, input().split()))
blacks = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(blacks[i] - whites[i], end=' ')