numbers = [5, 10]
for number in numbers:
    if number >=10:
        print(number)
        print('10이상')
    elif number <20:
        print(number)
        print('10미만')
print('----------------')
for number in numbers:
    if number <10:
        print('continue')
        continue
    elif number >=10:
        print(number)
        print('10이상')