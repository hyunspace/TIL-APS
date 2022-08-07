S = input()
# 첫번째 숫자(0 or 1)를 기준으로 다른 숫자를 만나는 횟수를 찾아서 각각 저장하기
one = 1
the_other = 0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        continue
    else:
        if S[i+1] == S[0]: # 첫 번째 숫자가 기준
            one += 1
        else:
            the_other += 1
print(min(one, the_other))