def run(In: str, Out: str):
    fileIn = open(In, "r")
    fileOut = open(Out, "w")
    # open source code

    number = int(fileIn.readline())
    tasks = []
    for i in range(number):
        a, b = [int(x) for x in fileIn.readline().split()]
        tasks += [[a, b]]

    tasks = sorted(tasks)
    res = 0
    beginTime = 0
    for task in tasks:
        res += task[1] - (beginTime + task[0])
        beginTime += task[0]

    # close source code
    fileOut.write(str(res))
    print(res, "finish")
    fileIn.close()
    fileOut.close()


# run("input0.txt", "output0.txt")
