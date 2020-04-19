def solve(n, arr):
    d = {}
    for i in range(n):
        d[i] = 0
    for i in arr:
        d[i - 1] += 1
    for v in d.values():
        print(v)

if __name__ == "__main__":
    n = int(input())
    arr = [int(s) for s in list(input().split())]
    solve(n ,arr)