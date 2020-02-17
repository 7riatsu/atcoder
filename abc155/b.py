def papers(n, arr):
    for ele in arr:
        if ele % 2 == 0:
            if ele % 3 == 0 or ele % 5 == 0:
                pass
            else:
                return 'DENIED'
        else:
            pass
    return 'APPROVED'

if __name__ == "__main__":
    n = int(input())
    arr = [int(s) for s in list(input().split())]
    print(papers(n, arr))