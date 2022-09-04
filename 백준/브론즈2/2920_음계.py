def define_notes(notes):
    if notes[0] == 1:
        cnt = 1
        for i in range(len(notes)):
            if notes[i] == cnt:
                cnt += 1
            else:
                return 'mixed'
        return 'ascending'
    elif notes[0] == 8:
        cnt = 8
        for i in range(len(notes)):
            if notes[i] == cnt:
                cnt -= 1
            else:
                return 'mixed'
        return 'descending'
    else:
        return 'mixed'

notes = list(map(int, input().split()))
print(define_notes(notes))