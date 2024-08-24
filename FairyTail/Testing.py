import random as rd
import FairyTail as main

BEGIN_TEST = int(input("BEGIN: "))
END_TEST = int(input("END: "))

for i_test in range(BEGIN_TEST, END_TEST):
    fileIn = open("input" + str(i_test) + ".txt", "w")
    inp = ""
    print("testcase begin: ", i_test)

    # generate input
    number = rd.randint(1, 10**5)  # ***
    inp += str(number) + "\n"
    # print(X, Y)
    # x = 1
    t = rd.randint(1, 10**5)
    d = rd.randint(1, 10**9)
    for i in range(number):
        t = rd.randint(1, 10**5)
        d = rd.randint(1, 10**9)
        inp += str(t) + " " + str(d) + "\n"
        # x += 300

    # close file
    fileIn.write(inp)
    fileIn.close()
    # run main
    main.run("input" + str(i_test) + ".txt", "output" + str(i_test) + ".txt")
