# while True:
#     number = int(input('number? '))
#     if number == 0:
#         break
#     elif number > 0 :
#         print('positive integer')
#     else:
#         print('negative number')

# total = 0
# cnt = 0
# while True:
#     number = int(input())
#     cnt += 1
#     total += number
#     if number >= 100:
#         print(total)
#         print(f'{total/cnt:.1f}')
#         break

# data = {'Korea': 'Seoul', 'USA': 'Washington', 'Japan': 'Tokyo', 'China': 'Beijing'}
# countries = list(data.keys())
# capitals = list(data.values())
#
# for idx in range(4):
#     print(countries[idx])

# odd_cnt = even_cnt = 0
# while True:
#     number = int(input())
#     if number == 0:
#         print(f'odd : {odd_cnt}\neven : {even_cnt}')
#     if number % 2:
#         odd_cnt += 1
#     else:
#         even_cnt += 1