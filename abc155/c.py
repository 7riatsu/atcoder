def poll(arr):
    ans_h = {}
    for ele in arr:
        if ele in ans_h.keys():
            ans_h[ele] += 1
        else:
            ans_h[ele] = 0
    max_v = max(ans_h.values())
    mkv = [kv for kv in ans_h.items() if kv[1] == max_v]
    for ele in sorted(mkv):
        print(ele[0])

if __name__ == "__main__":
    n = int(input())
    arr = [input() for _ in range(0, n)]
    poll(arr)