import math

def combinations_count(count, r):
    if count <= 1:
        return 0

    return math.factorial(count) // (math.factorial(count - r) * math.factorial(r))

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    print(combinations_count(n, 2) + combinations_count(m, 2))