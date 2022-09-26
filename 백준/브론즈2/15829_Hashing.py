r = 31
M = 1234567891

L = int(input())
text = input()
answer = 0
for i in range(L):
    answer += (ord(text[i]) - 96) * (r ** i)
print(answer%M)