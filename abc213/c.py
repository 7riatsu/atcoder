h, w, n = map(int, input().split())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x_dict = {ele: i + 1 for i, ele in enumerate(sorted(list(set(X))))}
y_dict = {ele: i + 1 for i, ele in enumerate(sorted(list(set(Y))))}

for i in range(n):
    print(x_dict[X[i]], y_dict[Y[i]])
