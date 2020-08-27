def solve(s):
    if "RRR" in s:
        return 3
    elif "RR" in s:
        return 2
    elif "R" in s:
        return 1
    else:
        return 0

if __name__ == "__main__":
    s = input()
    print(solve(s))