n = int(input())
cmds = [list(input()) for _ in range(n)]

answer = ''
for i in range(len(cmds[0])):
    temp = cmds[0][i]
    for j in range(n):
        if temp != cmds[j][i]:
            temp = '?'
    answer += temp
print(answer)