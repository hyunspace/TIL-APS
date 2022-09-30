from itertools import permutations

time = list(map(int, input().split(':')))
cases = permutations(time, 3)
answer = 0
for case in cases:
    if time != case and 1 <= case[0] <= 12 and 0 <= case[1] <= 59 and 0 <= case[2] <= 59:
        answer += 1
print(answer)