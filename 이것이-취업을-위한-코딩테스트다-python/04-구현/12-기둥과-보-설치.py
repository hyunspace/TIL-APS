def possibility(answer):
    for structure in answer:
        x, y, struc = structure
        # 기둥일 때
        if struc == 0:
            # 바닥 위에 있거나, 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있어야 함
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보일 때
        else:
            # 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 함
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, struc, install = build
        # 설치
        if install == 1:
            answer.append([x, y, struc])
            if not possibility(answer):
                answer.remove([x, y, struc])
        # 삭제
        else:
            answer.remove([x, y, struc])
            if not possibility(answer):
                answer.append([x, y, struc])
        # 최종 정렬
        answer.sort()
    return answer

# n = int(input())
# build_frame = [list(map(int, input().split())) for _ in range(8)]


# 1 0 0 1
# 1 1 1 1
# 2 1 0 1
# 2 2 1 1
# 5 0 0 1
# 5 1 0 1
# 4 2 1 1
# 3 2 1 1