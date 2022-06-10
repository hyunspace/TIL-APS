# text = input()
# for i in range(1, len(text)+1):
#     ans = ''
#     ans += text[-i:]
#     ans += text[0:-i]
#     print(ans)

# a = input()
# b = input()
# c = input()
#
# while True:
#     flag = 1
#     for idx in range(len(a) if len(a) <= len(b) else len(b)):
#         if a[idx] == b[idx]:
#             continue
#         elif a[idx] < b[idx]:
#             break
#         else:
#             flag = 0
#             break
#     if flag == 0:
#         print('NO')
#         break
#     for idx in range(len(b) if len(b) <= len(c) else len(c)):
#         if b[idx] == c[idx]:
#             continue
#         elif b[idx] < c[idx]:
#             break
#         else:
#             flag = 0
#             break
#     if flag:
#         print('YES')
#     else:
#         print('NO')
#     break

# 5번
# print(ord('cat'))

# aa, bb, cc = input().split()
# a, b, c = ord(aa[0]), ord(bb[0]), ord(cc[0])
# nums = [a, b, c]
# ans = [aa, bb, cc]
# min_num = min(nums)
# for idx in range(3):
#     if min_num == nums[idx]:
#         print(ans[idx])
#         break

# for a in aa:
#     nums[0] += ord(a)
# for b in bb:
#     nums[1] += ord(b)
# for c in cc:
#     nums[2] += ord(c)
#
# min_num = min(nums)
# ans = [aa, bb, cc]
# for idx in range(3):
#     if min_num == nums[idx]:
#         print(ans[idx])
#         break

# target = 'Pennsylvania'
# text = input().strip()
#
# if text in target:
#     print('True')
# else:
#     print('False')

# 형성평가1
# sentence = list(input().split('(space)'))
# for word in sentence[::-1]:
#     print(word.strip())

#2
# text, x, y = input().split()
# x = int(x)
# y = int(y)
# ans = text
# for i in range(y):
#     ans = ans[x::] + ans[0:x]
#     print(ans)

# while True:
#     word = input()
#     if word == 'END':
#         break
#     else:
#         print(word[::-1])

# 6번
text = input()
try:
    number = int(text)
    print('D')
    print(number)
except:
    if text.isupper():
        print('U')
        print(text)
    elif text.islower():
        print('L')
        print(text.upper())
    else:
        print('X')
        for t in text:
            try:
                print(int(t), end='')
            except:
                print(t.upper(), end='')