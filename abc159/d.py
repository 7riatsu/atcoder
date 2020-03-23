import math

past_ans = {}

def solve(arr):
    all_ans = {}
    for k in arr:
        print('====')
        print(past_ans)
        print(k)
        tmp_arr = []
        if k in past_ans:
            print(past_ans[k])
            continue
        else:
            tmp_arr.extend(arr)
            deleted_num = tmp_arr.pop(k)

            # 過去に計算していた場合
            if deleted_num in past_ans:
                print(past_ans[deleted_num])
                continue

            # 新しく計算する場合
            set_arr = []
            set_arr = list(set(tmp_arr))
            ans = 0
            for i in set_arr:
                # iを過去に計算していた場合, all_ansから取得する
                if i in all_ans:
                    ans += all_ans[i]
                else:
                    all_ans[i] = combinations_count(tmp_arr.count(i), 2)
                    ans += all_ans[i]
            past_ans[k] = ans
            print(ans)

def combinations_count(count, r):
    if count <= 1:
        return 0
    return math.factorial(count) // (math.factorial(count - r) * math.factorial(r))

if __name__ == "__main__":
    n = int(input())
    arr = [int(s) for s in list(input().split())]
    solve(arr)
