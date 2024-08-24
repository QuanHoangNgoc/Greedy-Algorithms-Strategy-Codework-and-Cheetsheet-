N_TEST = 100
import random as rd
import DNS as main

BEGIN_TEST = int(input("BEGIN: "))
END_TEST = int(input("END: "))


for i_test in range(BEGIN_TEST, END_TEST):
    fileIn = open("input" + str(i_test) + ".txt", "w")
    inp = ""
    print("testcase begin: ", i_test)

    # generate input
    n = rd.randint(10**2, 10**4)  # ***
    K = rd.randint(1, 5)  # ***
    Q = rd.randint(1, 10**5)  # ***
    inp += str(n) + " " + str(K) + " " + str(Q) + "\n"
    print(n, K, Q)
    for i in range(n):
        x, y, p = (
            rd.randint(0, 10**6),
            rd.randint(0, 10**6),
            rd.randint(1, K),
        )  # ***
        inp += str(x) + " " + str(y) + " " + str(p) + "\n"
    for i in range(Q):
        x, y = rd.randint(0, 10**6), rd.randint(0, 10**6)  # ***
        inp += str(x) + " " + str(y) + "\n"

    fileIn.write(inp)
    fileIn.close()

    # run main
    main.run("input" + str(i_test) + ".txt", "output" + str(i_test) + ".txt")
