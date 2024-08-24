def run(In: str, Out: str):
    fileIn = open(In, "r")
    fileOut = open(Out, "w")
    # open source code

    def func(a, b, C, K):
        return a * C + b * K

    a, b, N, X = [int(x) for x in fileIn.readline().split()]
    res = func(a, b, 0, 0)
    res = max(res, func(a, b, N, N))
    res = max(res, func(a, b, 0, X))
    res = max(res, func(a, b, X, 0))
    res = max(res, func(a, b, N, N - X))
    res = max(res, func(a, b, N - X, N))

    # close source code
    fileOut.write(str(res))
    print(res, "finish")
    fileIn.close()
    fileOut.close()


# run("input0.txt", "output0.txt")
