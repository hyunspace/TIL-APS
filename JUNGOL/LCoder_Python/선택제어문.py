# number = input('Number? ')
# if number == '1':
#     print('dog')
# elif number == '2':
#     print('cat')
# elif number == '3':
#     print('chick')
# else:
#     print("I don't know.")

# score = int(input("Score? ") )
# if score>=90:
#     print("Perfect")
# if score>=80:
#     print("Great")
# else:
#     print("Effort")

import time

now = time.localtime()
a = 0
a = now.tm_year - 1900  # ----------------------- ①
print(a, end=' ')
a += (now.tm_mon - 1)  # ----------------------- ②
print(a, end = ' ')
a += now.tm_mday
print(a, end = ' ')
# 위 문장에서 출력될 값들을 각각 ① ② ③위치에서의 a의 값으로 바꾸어 준다.