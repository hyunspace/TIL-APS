n = int(input())
f = int(input())

for i in range(0, 99):
    nn = n - n % 100
    nn += i
    if nn % f == 0:
        answer = nn % 100
        if answer > 9:
            print(answer)
        else:
            print(str(answer).zfill(2))
        break

