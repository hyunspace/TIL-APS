words = []
for _ in range(5):
    words.append(input())
w = input()
letter = input()
flag = 0
for word in words:
    if w == word or w in word or letter in word:
        flag = 1
        print(word)
if not flag:
    print('none')