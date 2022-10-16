import sys
input = sys.stdin.readline

def solution(n):
    result = [] # 연산 과정을 담을 곳
    nums = list(range(1, n+1)) # 대기 중인 숫자들
    stack = [] # 스택
    for i in range(n):
        num = int(input()) # 원하는 숫자
        # 대기열에 있다면
        if len(stack) == 0:
            # 일단 push
            while nums and num >= nums[0]:
                stack = [nums.pop(0)] + stack # 앞에 넣어야함
                result.append('+')
            # 넣었으면 빼기
            stack.pop(0)
            result.append('-')
        elif num > stack[0]:
            while nums and num >= nums[0]:
                stack = [nums.pop(0)] + stack # 앞에 넣어야함
                result.append('+')
            # 넣었으면 빼기
            stack.pop(0)
            result.append('-')
        elif num == stack[0]:
            # pop
            stack.pop(0)
            result.append('-')
        # 대기열에도 없고, 답이 없다!
        else:
            result = False
            return result
    return result

answer = solution(int(input()))
if answer:
    for i in answer:
        print(i)
else:
    print('NO')