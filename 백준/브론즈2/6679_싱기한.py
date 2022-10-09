answers = []
for i in range(1000, 10000):
    a = str(i)
    b = str(int(a, 12))
    c = str(int(a, 16))
    aa = bb = cc = 0
    for j in a:
        aa += int(j)
    for j in b:
        bb += int(j)
    for j in c:
        cc += int(j)
    if aa == bb == cc:
        answers.append(i)
for answer in answers:
    print(answer)
