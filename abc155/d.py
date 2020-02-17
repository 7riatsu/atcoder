import itertools
def pairs(k, arr):
    t_arr = list(itertools.combinations(arr, 2))
    a = sorted([t[0] * t[1] for t in t_arr])
    return a[k-1]
if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    arr = [int(s) for s in list(input().split())]
    print(pairs(k, arr))