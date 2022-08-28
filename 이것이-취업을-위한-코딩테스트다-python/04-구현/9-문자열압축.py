def text_compress(text, l):
    cut_text = [] # 잘라서 담아둘 리스트
    # 반복을 통해서 잘라서 리스트에 담기
    for i in range(0, len(text), l):
        cut_text.append(text[i:i + l])
    print(cut_text)
    cnt = 1 # 반복 횟수
    result = ''
    # 반복하기
    for j in range(len(cut_text)-1):
        # 다음 단어랑 같다면
        if cut_text[j] == cut_text[j+1]:
            # 숫자 세기
            cnt += 1
            if j == len(cut_text) - 2:
                result += str(cnt)
                result += cut_text[j]
        # 다르다면
        else:
            if cnt == 1: # 앞뒤로 동일 단어 X => 혼자서 둥둥
                result += cut_text[j]
            else: # cnt 숫자가 2 이상
                result += str(cnt)
                result += cut_text[j]
                cnt = 1 # 초기화
            # 아예 안 맞는 경우 남은 텍스트 그냥 더하기
            if j == len(cut_text) - 2:
                result += cut_text[j+1]
    print(result)
    return len(result)


def solution(s):
    answer = 1000
    for l in range(1, len(s)):
        length = text_compress(s, l)
        if answer > length:
            answer = text_compress(s, l)
    return answer

print(solution('aabbaccc'))