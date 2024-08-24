def isFeasible() -> bool:
    pass


def isBetter() -> bool:
    pass


n, S = map(int, input().split())
prices = list(map(int, input().split()))
prices = sorted(prices, key=lambda x: x)
# listOfSolution = []
res = 0
out = ""


def decodeWith(solution):
    # global listOfSolution
    # listOfSolution.append(solution)
    global out
    for i, j in enumerate(solution):
        for k in range(j):
            out += str(prices[i]) + " "
    out += "\n"


def tryTo(i: int, solution, currentCost: int, type: bool):
    if i == n or currentCost == S:
        # isFeasiable
        if currentCost == S:
            global res
            res += 1
            if type == True:
                decodeWith(solution=solution)
        return

    j_end = 0
    for j in range(100):
        # bound
        if currentCost + j * prices[i] > S:
            j_end = j
            break

    for j in range(j_end - 1, -1, -1):
        tryTo(
            i + 1,
            solution=solution + [j],
            currentCost=currentCost + j * prices[i],
            type=type,
        )


tryTo(0, solution=[], currentCost=0, type=True)
print(res)
print(out)
