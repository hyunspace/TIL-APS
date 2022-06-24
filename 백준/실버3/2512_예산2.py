# 5월 8일, 5월 9일

def find_budget(start, end, have): # 탐색 시작점, 끝점, 지금 가진 돈
    print(budgets)
    if have > 0 and end > 0 and start <= N:
        length = end - start    # 탐색 대상의 개수
        temp = have // length   # 현재 최적 상한액
        center = end // 2 - 1       # 중간 값
        if temp == 0:
            return
        print(f'center_idx:{center}, center:{budgets[center]}')
        print(f'start:{start}, end:{end}, have:{have}, temp:{temp}')
        if budgets[center] < temp:                  # 탐색값이 더 크다면
            print('첫번째 if문')
            for i in range(start, center + 1):      # 왼쪽 구간은 원하는 만큼 다 주기
                have -= budgets[i]
                budgets[i] = 0
                print(have)
            for j in range(center + 1, end):            # 오른쪽 구간은 탐색값만큼만
                if budgets[j] < temp:
                    have -= budgets[j]
                    budgets[j] = 0
                else:
                    have -= temp
                    budgets[j]-= temp
                print(have)
            find_budget(center + 1, end, have)          # 오른쪽 구간으로 이동

        elif budgets[center] == temp:               # 탐색값과 같다면 (왼쪽은 무조건 작음)
            print('두번째 if문')
            for i in range(start, center + 1):
                have -= budgets[i]
                budgets[i] = 0
                print(have)
            for j in range(center + 1, end):
                have -= temp
                budgets[j] -= temp
                print(f'have:{have}')
            print(budgets)
            find_budget(center + 1, end, have)

        else:                                        # 탐색값이 더 작다면
            print('세번째 if문')
            for i in range(start, center):
                if budgets[i] != 0 and budgets[i] < temp:
                    have -= budgets[i]
                    budgets[i] = 0
                    print(budgets)
                else:
                    have -= temp
                    budgets[i] -= temp
            for j in range(center, end):
                have -= temp
                budgets[j] -= temp
                print(temp, have)
            print(f'have:{have}')
            find_budget(start, end, have)


N = int(input())
budgets = sorted(list(map(int, input().split())))
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    beginning = sum(budgets)
    find_budget(0, N, M)

    print(beginning-sum(budgets))

