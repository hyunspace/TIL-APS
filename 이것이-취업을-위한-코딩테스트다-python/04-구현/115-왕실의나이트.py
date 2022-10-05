board = list([0]*8 for _ in range(8))
column_index = 'abcdefgh'
now = input()
direction = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
current_column = column_index.find(now[0])
current_row = int(now[1]) - 1
answer = 0
for d in direction:
    new_column = current_column + d[0]
    new_row = current_row + d[1]
    if 0<= new_column < 8 and 0<= new_row < 8:
        answer += 1
print(answer)
