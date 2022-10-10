# from itertools import combinations
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))
# height = max(trees) - 1
#
# def find_tree_height():
#     global height
#     temp = []
#     for tree in trees:
#         if tree - height > 0:
#             temp.append(tree-height)
#     if sum(temp) == m:
#         print(height)
#         return
#     elif sum(temp) < m:
#         height -= 1
#         find_tree_height()
#     else:
#         cases = combinations(temp)
#         for case in cases:
#             if sum(case) == sum(temp):
#                 print(height)
#                 return
#
# find_tree_height()

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)

while start <= end:
    center = (start + end) // 2
    cut_tree = 0
    for tree in trees:
        if tree - center > 0:
            cut_tree += tree - center
        if cut_tree > m:
            break
    if cut_tree < m:
        end = center - 1
    else:
        start = center + 1
print(end)
