def solve(n, m, arr):
    arr.sort()
    for i in range(m):
        if arr[-1 - i] < sum(arr) * (1 / (4 * m)):
            return False
    return True

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    arr = [int(s) for s in list(input().split())]
    if solve(n, m, arr):
        print('Yes')
    else:
        print('No')
