N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

for i in range(0 if N == 1 else 10 ** (N - 1), 10 ** N):
    i_str = str(i)
    for s, c in arr:
        if i_str[s - 1] != str(c):
            break
    else:
        print(i)
        break
else:
    print(-1)
