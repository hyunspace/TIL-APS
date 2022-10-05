N, M = map(int, input().split())
balls = list(map(int, input().split()))
cnt = 0
# 예제 설명을 그대로 코드로 옮기기..!
for i in range(N-1):
    for j in range(i+1, N):
        # 다음 공이 다른 무게면 조합 만들기
        if balls[i] != balls[j]:
            cnt += 1
print(cnt)