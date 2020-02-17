def poor(arr):
    if len(set(arr)) == 2:
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    arr = [int(s) for s in list(input().split())]
    print(poor(arr))