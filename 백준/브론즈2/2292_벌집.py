n = int(input())
answer = 1
def find_rooms():
    global answer
    if n == 1:
        answer = 1
        return
    end = 1
    while n > end:
        end += 6 * answer
        answer += 1

find_rooms()
print(answer)