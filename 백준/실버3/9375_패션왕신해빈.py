# from itertools import combinations
#
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     costume = {}
#     for _ in range(n):
#         clothe, category = input().split()
#         try:
#             costume[category].append(clothe)
#         except:
#             costume[category] = [clothe]
#     cases = list(costume.values())
#     answer = 1
#     if len(cases) == 1:
#         answer = len(cases[0])
#     else:
#         temp = 0
#         for case in cases:
#             answer *= len(case)
#             temp += len(case)
#         answer += temp
#     print(answer)
#

