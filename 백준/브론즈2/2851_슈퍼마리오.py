
def supermario():
    cnt = 0
    for i in range(10):
        num = int(input())
        cnt += num
        if cnt == 100:
            print(cnt)
            return
        if cnt > 100:
            if (cnt - 100) <= (100 - cnt + num):
                print(cnt)
                return
            else:
                print(cnt-num)
                return
    print(cnt)
    return

supermario()
