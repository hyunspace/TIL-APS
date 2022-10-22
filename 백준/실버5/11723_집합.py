import sys
input = sys.stdin.readline

m = int(input())
S = [0] * 21
for _ in range(m):
    cmd = input().rstrip()
    if cmd == 'all':
        S = [1] * 21
    elif cmd == 'empty':
        S = [0] * 21
    else:
        cmd, num = cmd.split()
        num = int(num)
        if cmd == 'add':
            S[num] = 1
        elif cmd == 'remove':
            S[num] = 0
        elif cmd == 'check':
            if S[num]:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if S[num]:
                S[num] = 0
            else:
                S[num] = 1

# S = set()
# for _ in range(m):
#     cmd = input().rstrip()
#     if cmd == 'all':
#         S = {range(1, 21)}
#     elif cmd == 'empty':
#         S = set()
#     else:
#         cmd, num = cmd.split()
#         if cmd == 'add':
#             if not num in S:
#                 S.add(num)
#         elif cmd == 'remove':
#             if num in S:
#                 S.remove(num)
#         elif cmd == 'check':
#             if num in S:
#                 print(1)
#             else:
#                 print(0)
#         elif cmd == 'toggle':
#             if num in S:
#                 S.remove(num)
#             else:
#                 S.add(num)