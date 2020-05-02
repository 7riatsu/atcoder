def solve(k, a, b):
    for i in range(a, b+1):
        if i % k == 0:
            return 'OK'
    return 'NG'

if __name__ == "__main__":
    k = int(input())
    a, b = map(int, input().split(' '))
    print(solve(k, a, b))