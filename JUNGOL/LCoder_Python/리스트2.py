#1번

# scores = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
# a, b = map(int, (input().split()))
#
# print(f'{scores[a - 1] + scores[b - 1]:.1f}')


# 2번
# words = []
# for _ in range(5):
#     words.append(input())
#
# for idx in range(4, -1, -1):
#     print(words[idx])


# 3번
# words = []
# for _ in range(10):
#     words.append(input())
# letter = input()
#
# for word in words:
#     if word[len(word)-1] == letter:
#         print(word)


# 4번
# numbers = list(map(int, input().split()))
# print(min(numbers))


#5번
# numbers = list(map(int, input().split()))
# min_num = 10000
# max_num = 1
# for number in numbers:
#     if number >= 100 and min_num >= number:
#         min_num = number
#     elif number < 100 and max_num < number:
#         max_num = number
# if min_num == 10000 and max_num == 1:
#     print(100, 100)
# elif min_num == 10000:
#     print(max_num, 100)
# elif max_num == 1:
#     print(100, min_num)
# else:
#     print(max_num, min_num)


#6번
# numbers = list(map(int, input().split()))
# odds = evens = 0
#
# for idx in range(10):
#     if idx % 2:
#         evens += numbers[idx]
#     else:
#         odds += numbers[idx]
#
# print(f'sum : {evens}')
# print(f'avg : {odds/5:.1f}')


# 7번
# numbers = list(map(int, input().split()))
# numbers.sort(reverse=True)
# print(*numbers)


# 8번
# text = list(input() for _ in range(5))
# text.sort(reverse=True)
# for t in text:
#     print(t)


# 형성평가
# 1번
# numbers = []
# while True:
#     number = int(input())
#     if number == -1:
#         break
#     else:
#         numbers.append(number)
#
# length = len(numbers)
# if length < 3:
#     for num in numbers:
#         print(num, end=' ')
# else:
#     for idx in range(length-3, length):
#         print(numbers[idx], end =' ')


# 2번
# weight = list(map(float, input().split()))
# print(f'{sum(weight) / 6:.1f}')


# 3번
# texts = ['J', 'U', 'N', 'G', 'O', 'L']
# text = input()
# if text not in texts:
#     print('none')
# else:
#     print(texts.index(text))


# 4번
# numbers = list(map(int, input().split()))
# print(f'max : {max(numbers)}')
# print(f'min : {min(numbers)}')

# max_num = min_num = numbers[0]
# for number in numbers:
#     if max_num < number:
#         max_num = number
#     if min_num > number:
#         min_num = number
#
# print(f'max : {max_num}')
# print(f'min : {min_num}')


# 5번
# numbers = list(map(int, input().split()))
# total = cnt = 0
# for num in numbers:
#     if num % 5 == 0:
#         total += num
#         cnt += 1
# print(f'Multiples of 5 : {cnt}')
# print(f'sum : {total}')
# print(f'avg : {total/cnt:.1f}')


# 6번
# numbers = list(map(int, input().split()))
# print(len(numbers))
# for num in numbers:
#     if num % 2:
#         print(num*2, end=' ')
#     else:
#         print(num//2, end=' ')


# 7번
# n = int(input())
# scores = list(map(int, input().split()))
# scores.sort(reverse=True)
# for score in scores:
#     print(score)


# 8번
# words = ["flower", "rose", "lily", "daffodil", "azalea"]
# letter = input()
# cnt = 0
# for word in words:
#     if word[1] == letter or word[2] == letter:
#         print(word)
#         cnt += 1
# print(cnt)


# 9번
# words = []
# cnt = 0
# while True:
#     word = input()
#     if word == '0':
#         break
#     else:
#         cnt += 1
#         if 'mo' in word:
#             words.append(word)
# print(cnt)
# for w in words:
#     print(w)


# 10번
# words = []
# for _ in range(5):
#     words.append(input())
# w = input()
# letter = input()
# flag = 0
# for word in words:
#     if w == word or w in word or letter in word:
#         flag = 1
#         print(word)
# if not flag:
#     print('none')
