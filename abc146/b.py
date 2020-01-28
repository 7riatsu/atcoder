def rot(n, s):
    result = ""
    for i in s:
        result += chr(ord("A") + (ord(i) - ord("A") + n) % 26)
    return result

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(rot(n, s))
    # arr = list(s)
    # print(n, arr)