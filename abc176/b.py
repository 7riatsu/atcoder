def solve(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    n = input()
    print(solve(n))