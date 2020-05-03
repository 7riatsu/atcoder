def solve(n, k, d_arr, arr):
    ans = []
    for _ in range(n):
        ans.append(0)

    for i in range(k):
        ele = arr[i]
        for j in arr[i]:
            ans[j-1] += 1
    return ans.count(0)

if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    d_arr = []
    arr = []
    for _ in range(k):
        d_arr.append(int(input()))
        arr.append([int(s) for s in list(input().split())])
    print(solve(n, k, d_arr, arr))