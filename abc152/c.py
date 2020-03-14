def low_elements(n, arr):
    min = arr[0]
    count = 0
    for i in range(n):
        if min >= arr[i]:
            min = arr[i]
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(low_elements(n, arr))