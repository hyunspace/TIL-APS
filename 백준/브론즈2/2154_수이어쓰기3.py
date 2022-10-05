n = int(input())
n_len = len(str(n))
new_num = ''
for i in range(1, n+1):
    new_num += str(i)
for j in range(0, len(new_num)-n_len+1):
    if new_num[j:j+n_len] == str(n):
        print(j+1)
        break