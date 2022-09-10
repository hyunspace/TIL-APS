tc = int(input())
for _ in range(tc):
    h, w, n = map(int, input().split())
    ch = 0
    cw = 1
    room = 0
    for i in range(1, n+1):
        if 0 <= ch < h:
            ch += 1
            room = ch * 100 + cw
            print(room, end=' ')
        else:
            ch = 1
            cw += 1
            room = ch * 100 + cw
            print(room)
    print()
    print('---------------')
    # print(room)

# tc = int(input())
# for _ in range(tc):
#     h, w, n = map(int, input().split())
#     ch = cw = 1
#     room = 0
#     for i in range(1, n+1):
#         if 1 <= ch < h:
#             room = ch * 100 + cw
#             ch += 1
#             print(room, end=' ')
#         else:
#             ch = 1
#             cw += 1
#             room = ch * 100 + cw
#             print(room)
#     print('----------------')
