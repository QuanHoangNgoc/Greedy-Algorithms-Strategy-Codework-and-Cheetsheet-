def intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if denominator == 0:
        return False  # lines are parallel

    px = (
        (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    ) / denominator
    py = (
        (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    ) / denominator

    if (
        min(x1, x2) <= px <= max(x1, x2)
        and min(x3, x4) <= px <= max(x3, x4)
        and min(y1, y2) <= py <= max(y1, y2)
        and min(y3, y4) <= py <= max(y3, y4)
    ):
        return True  # lines intersect
    else:
        return False  # lines do not intersect


import random as rd

N = int(input())
lines = []
flag = False
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    line = [[x1, y1], [x2, y2]]
    lines.append([[x1, y1], [x2, y2], i + 1])


def keyFunc(a):
    if a[1][0] - a[0][0] == 0:
        return 1e9
    return (a[1][1] - a[0][1]) / (a[1][0] - a[0][0])


lines = sorted(lines, key=keyFunc)

print(lines)


for i in range(N):
    for j in range(max(0, i - 100), i):
        if intersect(lines[i], lines[j]):
            print(lines[i][2])
            exit()
