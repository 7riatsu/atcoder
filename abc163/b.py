def solve(n, m, arr):
    ans = n - sum(arr)
    if ans >= 0:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    arr = [int(s) for s in list(input().split())]
    solve(n, m, arr)