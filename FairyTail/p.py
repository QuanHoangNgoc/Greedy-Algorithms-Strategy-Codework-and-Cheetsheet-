number = int(input())
tasks = []
for i in range(number):
    a, b = [int(x) for x in input().split()]
    tasks += [[a, b]]

tasks = sorted(tasks)
res = 0
beginTime = 0
for task in tasks:
    res += task[1] - (beginTime + task[0])
    beginTime += task[0]

print(res)
