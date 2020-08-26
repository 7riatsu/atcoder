def solve(n, arr):
    ans_arr = [0]
    for i in range(0, n-1):
        if arr[i] > arr[i + 1]:
            diff = arr[i] - arr[i + 1]
            ans_arr.append(diff)
            arr[i + 1] += diff
        else:
            ans_arr.append(0)
    return sum(ans_arr)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(solve(n, arr))