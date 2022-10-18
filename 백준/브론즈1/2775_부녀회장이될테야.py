def bring_people():
    for i in range(0, k):
        temp = 0
        for j in range(1, n+1):
            temp += apt[i][j]
            apt[i+1][j] = temp

tc = int(input())
for _ in range(tc):
    # k층 n호
    k = int(input())
    n = int(input())
    apt = [[0] * (n+1) for _ in range(k+1)]
    # 0층 채우기
    for i in range(n+1):
        apt[0][i] = i
    # 목표까지 채우기
    bring_people()
    print(apt[k][n])