a, b, v = map(int, input().split())
days = 0
# def snail():
#     global days
#     height = 0
#     cnt = 0
#     while height < v:
#         cnt += 1
#         height += a
#         print(cnt, height)
#         if height >= v:
#             days += 1
#             return
#         height -= b
#         days += 1
#     return

def snail():
    global days, v
    v -= a
    if v % (a - b) == 0:
        days = v // (a - b) + 1
    # elif (v % (a - b)) <= a:
    else:
        days = v // (a - b) + 2

snail()
print(days)
