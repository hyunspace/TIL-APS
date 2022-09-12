import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    if target in nums:
        print(1)
    else:
        print(0)