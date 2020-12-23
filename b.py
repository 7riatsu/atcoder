s = input()

while len(s) > 0:
    s = s[:-1]
    half_idx = int(len(s) / 2)
    if len(s) % 2 == 0 and s[:half_idx] == s[half_idx:]:
        print(len(s))
        exit()