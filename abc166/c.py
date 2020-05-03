def solve(n, m, h_arr, arr):
    count = 0
    ans_hash = {}
    for ele in range(1, n+1):
        ans_hash[ele] = []
    # iは ans_hash のindex
    for i in range(1, m + 1):
        # jは arr の要素一つずつ取り出したもの
        for j in arr[i - 1]:
            if h_arr[j-1] != h_arr[i-1]:
                ans_hash[i].append(h_arr[j-1])
    print(ans_hash)

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    h_arr = list(map(int, input().split(' ')))
    arr = []
    for _ in range(m):
        arr.append([int(s) for s in list(input().split())])
    print(solve(n, m, h_arr, arr))