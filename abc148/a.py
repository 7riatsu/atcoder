def round_one(arr):
    ans_candidates = [1,2,3]
    for c in ans_candidates:
        if c in arr:
            pass
        else:
            print(c)


if __name__ == "__main__":
    a = [int(input()) for i in range(2)]
    round_one(a)