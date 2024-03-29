# https://qiita.com/gogotealove/items/11f9e83218926211083a#%E4%BE%8B%E9%A1%8C-1
# bit全探索の例

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]  # 買い物累計額にも加算
    if (total <= money):
        print(total, bag)
