import random as rd
import Naruto as main

BEGIN_TEST = int(input("BEGIN: "))
END_TEST = int(input("END: "))

for i_test in range(BEGIN_TEST, END_TEST):
    fileIn = open("input" + str(i_test) + ".txt", "w")
    inp = ""
    print("testcase begin: ", i_test)

    # generate input
    A = 10**3
    a, b = rd.randint(-A, A), rd.randint(-A, A)
    X = rd.randint(1, 10**3)
    N = rd.randint(0, 10**5) * X * 2
    inp += str(a) + " " + str(b) + " " + str(N) + " " + str(X)
    print(a, b, N, X)

    # close file
    fileIn.write(inp)
    fileIn.close()
    # run main
    main.run("input" + str(i_test) + ".txt", "output" + str(i_test) + ".txt")
