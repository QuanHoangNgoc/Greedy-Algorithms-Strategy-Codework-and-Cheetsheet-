N_TEST = 100
import random as rd
import OnePiece as main

for i_test in range(N_TEST):
    fileIn = open("input" + str(i_test) + ".txt", "w")
    inp = ""
    print("testcase begin: ", i_test)

    # generate input
    number = rd.randint(1, 10**5)  # ***
    numK = rd.randint(1, number)  # ***
    print(number, numK)
    inp += str(number) + " " + str(numK) + "\n"
    X = rd.choices(range(1, 10**6), k=number)
    Y = rd.choices(range(1, 10**6), k=number)
    # print(X, Y)
    for i in range(number):
        inp += str(X[i]) + " " + str(Y[i]) + "\n"
    fileIn.write(inp)
    fileIn.close()

    # run main
    main.run("input" + str(i_test) + ".txt", "output" + str(i_test) + ".txt")
