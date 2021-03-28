# Solve with bit full search
n = input()
op_cnt = len(n) - 1

for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"
    formula = ""
    for p_n, p_o in zip(n, op + [""]):
        formula += (p_n + p_o)
    if eval(formula) == 7:
        print(formula + "=7")
        break


# Solve with nested loop
# s = input()
# ans = ''

# for i in ["-", "+"]:
#     for j in ["-", "+"]:
#         for k in ["-", "+"]:
#             tmp = s[0] + i + s[1] + j + s[2] + k + s[3]
#             if eval(tmp) == 7:
#                 ans = tmp + '=7'
# print(ans)