lst = list(int(input()) for _ in range(5))
l = lst[0]
if lst[1] % lst[3]:
    korean = lst[1] // lst[3] + 1
else:
    korean = lst[1] // lst[3]
if lst[2] % lst[4]:
    math = lst[2] // lst[4] +1
else:
    math = lst[2] // lst[4]
if korean >= math:
    print(l-korean)
else:
    print(l-math)