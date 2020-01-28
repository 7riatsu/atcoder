def kaibun(arr):
    count = 0
    arr_len = len(arr) - 1

    if arr_len % 2 == 0:
        for i in range(0, int(arr_len / 2)):
            if arr[i] != arr[arr_len-i]:
                count += 1
        return count
    else:
        for i in range(0, int((arr_len + 1) / 2)):
            if arr[i] != arr[arr_len-i]:
                count += 1
        return count


if __name__ == "__main__":
    s = input()
    arr = list(s)
    print(kaibun(arr))