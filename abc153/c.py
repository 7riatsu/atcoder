# こっちだとTLEする
# def attack(h, k, arr):
#     for _ in range(k):
#         if len(arr) == 0:
#             return 0
#         arr.remove(max(arr))
#     return sum(arr)

# if __name__ == "__main__":
    # h, k = map(int, input().split())
    # arr = list(map(int,input().split()))
    # print(attack(h, k, arr))

def attack(h, k, arr):
    arr.sort()
    if h - k > 0:
        return sum(arr[0:h-k])
    else:
        return 0

if __name__ == "__main__":
    h, k = map(int, input().split())
    arr = list(map(int,input().split()))
    print(attack(h, k, arr))