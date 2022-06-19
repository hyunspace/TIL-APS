#941
# words = ('Forest', 'Ocean', 'Mountain', 'Plain')
# num = int(input())
# if 1 <= num <= 4:
#     print(words[num-1])
# else:
#     print('Input Error')


# 942
# data = [('Dolphin','Oh My Girl'), ('Pallette','IU'), ('Yes or Yes', 'Twice')]
# print('[Song by Artist]\n==========')
# for d in data:
#     print(f'{d[0]} by {d[1]}')


# 943
# n = int(input())
# for _ in range(n):
#     game_id, win, rank = input().split()
#     if (rank != 'Bronze' and float(win) >= 60.0) or rank == 'Platinum':
#         print(f'[Gosu] {game_id}')


# 944
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# c = set(map(int, input().split()))
#
# print(f'Intersection: {a & b & c}')
# print(f'Union: {a | b | c}')


# 945
# qna = {'Pokemon': 'Pikachu', 'Digimon': 'Agumon', 'Yugioh': 'Black Magician'}
# question = input()
# if question in qna:
#     print(qna[question])
# else:
#     print("I don't know")


# 946
# n = int(input())
# data = {}
# for _ in range(n):
#     country, capital = input().split()
#     data[country] = capital
# question = input()
# if question in data:
#     print(data[question])
# else:
#     print('Unknown Country')


# 947
# awarded = list(input().split())
# num = int(input())
# records = {}
# for name in awarded:
#     if name in records:
#         records[name] += 1
#     else:
#         records[name] = 1
# for name in records:
#     if records[name] == num:
#         print(name)


# 948
# a, b, c = map(float, input().split())
# ans = (round(a+b+c, 3), round(a*b*c, 3))
# print(ans)


# 949
# n = int(input())
# ans = []
# for _ in range(n):
#     a, b = input().split()
#     ans.append((a, b))
# print(ans)


# 950
# cars = set(input().split())
# cars = list(cars)
# print(*sorted(cars))
# print(len(cars))


# 951
# first = set(map(int, input().split()))
# second = set(map(int, input().split()))
# ans = first - second
# print(*sorted(ans))


# 952
# n = int(input())
# dict = {}
# for _ in range(n):
#     dict_key, dict_value = input().split()
#     dict[dict_key] = dict_value
# print(dict[input()])


# 953
# records = list(input().split())
# foul_cnt = {}
# min_foul = len(records)
# for player in records:
#     if player in foul_cnt:
#         continue
#     else:
#         foul_cnt[player] = records.count(player)
#         if min_foul > records.count(player):
#             min_foul = records.count(player)
#
# for player in foul_cnt:
#     if foul_cnt[player] == min_foul:
#         print(player)
# print(min_foul)
