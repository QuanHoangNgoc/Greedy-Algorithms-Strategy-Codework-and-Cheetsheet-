def func(a, b, C, K):
    return a * C + b * K


a, b, N, X = [int(x) for x in input().split()]
res = func(a, b, 0, 0)
res = max(res, func(a, b, N, N))
res = max(res, func(a, b, 0, X))
res = max(res, func(a, b, X, 0))
res = max(res, func(a, b, N, N - X))
res = max(res, func(a, b, N - X, N))
print(res)
