while True:
    question = input()
    if question[0] == '#':
        break
    alphabet = question[0]
    upper_alphabet = alphabet.upper()
    sentence = []
    sentence.extend(question[2::])
    answer = 0

    for char in sentence:
        if char == alphabet or char == upper_alphabet:
            answer += 1
    print(alphabet, answer)