def check(P: int, a: list, b: list, numK: int) -> bool:
    v = []
    for i in range(len(a)):
        v += [b[i] - a[i] * P]

    v = sorted(v)
    v = v[::-1]

    sum = 0
    for i in range(min(numK, len(v))):
        sum += v[i]

    return sum >= 0


number, numK = [int(x) for x in input().split()]
a, b = [], []
for i in range(number):
    __a, __b = [int(x) for x in input().split()]
    a += [__a]
    b += [__b]

d = 1
c = int(2e6)
res = 0
while d <= c:
    p = (d + c) // 2
    if check(p, a, b, numK=numK):
        res = p
        d = p + 1
    else:
        c = p - 1
# fileOut.write(str(res))
# print(res, "finish")'
print(res)
# fileIn.close()
# fileOut.close()
