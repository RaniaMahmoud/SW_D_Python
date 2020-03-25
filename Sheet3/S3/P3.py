def F1(x):
    def F2(x):
        print("F2{}".format(x))
    F2(x)
    print("F1{}".format(x))

F1(2)