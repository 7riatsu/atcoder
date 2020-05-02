def solve(n, m, q, arr):
    i = 0
    for j in range(q):
        print(arr[j])
        if arr[j][1] - arr[j][0] == arr[j][2]:
            print('here')
            i += arr[j][3]
    return i

if __name__ == "__main__":
    n, m, q = map(int, input().split(' '))
    arr = []
    for _ in range(q):
        arr.append([int(s) for s in list(input().split())])
    print(solve(n, m, q, arr))