def attack(h, n, arr):
    h -= sum(arr)
    if h <= 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    h, n = map(int, input().split())
    arr = list(map(int,input().split()))
    print(attack(h, n, arr))