# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))
#
# height = sum(trees) // n
#
# while True:
#     answer = 0
#     for tree in trees:
#         if tree > height:
#             answer += tree - height
#     if answer == m:
#         print(height)
#         break
#     elif answer > m:
#         height = (height + max(trees)) // 2
#     # else:
#         height = (height + min(trees)) // 2
