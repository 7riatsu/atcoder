n_arr = []
m_arr = []
ans = 0

n = int(input())
for _ in range(n):
    n_arr.append(input())

m = int(input())
for _ in range(m):
    m_arr.append(input())

for char in set(n_arr):
    ans = max(ans, n_arr.count(char) - m_arr.count(char))
print(ans)