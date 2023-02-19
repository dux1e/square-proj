for x in range(5):
    for n in range(5):
        # upper left corner
        if x == 0 and n == 0:
            print("+", end="")
        # upper right corner
        if x == 0 and n == 4:
            print("+")
        # lower left corner
        if x == 4 and n == 0:
            print("+", end="")
        # lower right corner
        if x == 4 and n == 4:
            print("+")