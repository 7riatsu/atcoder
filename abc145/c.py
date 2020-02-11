def average_length(s, t, a, b, u):
    if u == s:
        return a - 1, b
    elif u == t:
        return a, b - 1
    return

if __name__ == "__main__":
    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input()
    print(average_length(s, t, a, b, u))