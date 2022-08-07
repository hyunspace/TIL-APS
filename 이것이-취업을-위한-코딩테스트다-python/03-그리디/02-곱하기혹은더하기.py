S = input()
ans = 0
for i in S:
    # 0을 곱하면 그동안 구한 값이 0이 되므로 무조건 더해야 하고,
    # 1을 곱하면 숫자가 그대로지만 더하면 더 커지므로, 1일 때는 더해야 함
    if i == '0' or ans == 0 or i == '1':
        ans += int(i)
    # 그 외의 경우에는 항상
    else:
        ans *= int(i)
print(ans)