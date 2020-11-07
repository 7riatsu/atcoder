n, m = map(int, input().split())

ac_cnt = 0
wa_cnt = 0
results = [['WA', 0] for _ in range(n + 1)]

for _ in range(m):
    p, r = input().split()
    p = int(p)

    if results[p][0] == 'WA':
        if r == 'WA':
            results[p][1] += 1
        else:
            wa_cnt += results[p][1]
            results[p][0] = 'AC'
            ac_cnt += 1

print(ac_cnt, wa_cnt)