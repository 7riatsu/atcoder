s = input()

l_a = s.count("a")
l_b = s.count("b")
l_c = s.count("c")

if abs(l_a - l_b) <= 1 and abs(l_b - l_c) <= 1 and abs(l_c - l_a) <= 1:
    print("YES")
else:
    print("NO")
