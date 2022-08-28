txt = input()
num = 0
alphabet = []

for t in txt:
    try:
        num += int(t)
    except:
        alphabet += t

sorted_txt = ''.join(sorted(alphabet))
print(sorted_txt, end='')
print(num)
