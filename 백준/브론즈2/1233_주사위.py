from itertools import product

s1, s2, s3 = map(int, input().split())
nums = [list(range(1, s1+1)), list(range(1, s2+1)), list(range(1, s3+1))]
pick_cases = list(product(*nums))
sum_cases = {}
for pick_case in pick_cases:
    try:
        sum_cases[sum(pick_case)] += 1
    except:
        sum_cases[sum(pick_case)] = 1

sorted_sum = sorted(sum_cases.items(), key=lambda x:(x[1], -x[0]), reverse=True)
print(sorted_sum[0][0])