def find_m(n):
    for i in range(1, n):
        m = i
        str_i = str(i)
        for j in str_i:
            m += int(j)
        if m == n:
            return i
    return 0

n = int(input())

print(find_m(n))