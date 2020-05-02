import math

def solve(a, b, n):
    ans_arr = []
    for i in reversed(range(1, n + 1)):
        value = math.floor(a * i / b) - a * math.floor(i / b)
        if value == 0:
            next
        else:
            return value

if __name__ == "__main__":
    a, b, n = map(int, input().split(' '))
    print(solve(a,b,n))