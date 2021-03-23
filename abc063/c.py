n = int(input())
arr = sorted([int(input()) for _ in range(n)])
ans = sum(arr)

if ans % 10 == 0:
    for ele in arr:
        if ele % 10 != 0:
            ans -= ele
            print(ans)
            exit()
    print(0)
    exit()
print(ans)
