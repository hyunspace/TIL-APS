text = []
text.extend(input())
for char in text:
    if char.isupper():
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')