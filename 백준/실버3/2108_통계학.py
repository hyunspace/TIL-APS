import sys
input = sys.stdin.readline

n = int(input())
nums = []
num_cnt = {}
for _ in range(n):
    num = int(input())
    nums.append(num)
    try:
        if num_cnt[num] >= 1:
            num_cnt[num] += 1
    except:
        num_cnt[num] = 1
nums.sort()
print(int(round(sum(nums)/n, 0))) #산술평균
print(nums[n//2]) #중앙값
sorted_cnt = sorted(num_cnt.items(), key = lambda x:(-x[1], x[0]))
if len(sorted_cnt) > 1 and sorted_cnt[0][1] == sorted_cnt[1][1]:
    print(sorted_cnt[1][0]) #최빈값
else:
    print(sorted_cnt[0][0])
print(nums[-1]-nums[0]) #범위