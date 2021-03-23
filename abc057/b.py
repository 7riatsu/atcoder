n, m = map(int, input().split())

students = []
for _ in range(n):
    a, b = map(int, input().split())
    students.append((a, b))

checkpoints = []
for _ in range(m):
    c, d = map(int, input().split())
    checkpoints.append((c, d))

ans = []

for student in students:
    i = 0
    tmp_d = 10e8 * 2 * 2
    for k, checkpoint in enumerate(checkpoints):
        d = abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1])
        if tmp_d <= d:
            pass
        else:
            tmp_d = d
            i = k + 1
    ans.append(i)

for ele in ans:
    print(ele)