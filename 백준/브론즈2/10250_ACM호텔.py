tc = int(input())
for _ in range(tc):
    h, w, n = map(int, input().split())
    ch = cw = 1
    distance = 1
    room = []
    rooms = []
    for i in range(1, n+1):
        if i == 1:
            room = [ch, cw]