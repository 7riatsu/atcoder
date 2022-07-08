# brute force
a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
	l = list(str(i))
	for c in l:
		if c == '4' or c == '9':
			ans += 1
			break
print(ans)
