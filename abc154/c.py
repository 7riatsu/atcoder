def has_duplicates(arr):
    if len(arr) != len(set(arr)):
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    n = int(input())
    arr = input().split()
    print(has_duplicates(arr))