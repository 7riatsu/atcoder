def solve(n, k):
    mod = n % k
    if mod == 0:
        print(0)
    elif abs(mod - k) < mod:
        print(abs(mod - k))
    else:
        print(mod)

if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    solve(n, k)