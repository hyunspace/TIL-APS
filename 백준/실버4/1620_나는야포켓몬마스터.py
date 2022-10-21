import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0]
dict = {}
for i in range(n):
    name = input().strip()
    lst.append(name)
    dict[name] = i+1
for _ in range(m):
    question = input().strip()
    try:
        # 숫자라면
        question = int(question)
        print(lst[question])
    except:
        print(dict[question])