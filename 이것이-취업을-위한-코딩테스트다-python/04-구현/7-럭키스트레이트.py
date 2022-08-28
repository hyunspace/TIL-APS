n = input()
center = int(len(n)/2)
left = n[0:center]
right = n[center::]

left_sum = right_sum = 0
# for l in left:
#     left_sum += int(l)
# for r in right:
#     right_sum += int(r)

for i in range(center):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
