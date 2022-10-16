# a, b, c, d, e, f = map(int, input().split())
# if a*e != b*d:
#     y = (a*f-c*d) // (a*e-b*d)
# else:
#     y = 
# x = (c-b*y)//a
# print(x, y)

n = int(input())
while True:
    test = str(n)
    flag = 1
    for t in test:
        if t in '47':
            continue
        else:
            flag = 0
            break
    if flag:
        print(n)
        break
    else:
        n -= 1
    
