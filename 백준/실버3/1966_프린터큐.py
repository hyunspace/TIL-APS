from collections import deque

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    index = list(i for i in range(n))
    docs = list(map(int, input().split()))
    cnt = 0
    while docs:
        if docs[0] != max(docs):
            docs.append(docs[0])
            docs = docs[1::]
            index.append(index[0])
            index = index[1::]
        else:
            cnt += 1
            if index[0] == m:
                print(cnt)
                break
            else:
                docs.pop(0)
                index.pop(0)
        # if docs[0] == max(docs):
        #     if index[0] == m:
        #         cnt += 1
        #         print(f'#{tc+1} cnt')
        #         break
        #     else:
        #         docs.pop()
        #         index.pop()
        #         cnt += 1
        # else:
        #     out_docs = docs.pop()
        #     out_index = docs.pop()
        #     docs.append(out_docs)
        #     index.append(out_index)





    # temp = list(map(int, input().split()))
    # docs = []
    # for i in range(n):
    #     docs.append([i, temp[i]])
    # docs.sort(reverse=True, key = lambda x : x[1])
    # print(docs)
    # for j in range(n):
    #     if docs[j][0] == m:
    #         print(j+1)
    #         break



