print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end="")

def butterfly(row):
    for i in range(row):
        for k in range(i):
            print_star()

        for j in range(2*row - 2*i):
            print_space()

        for k in range(i):
            print_star()
        next_line()

    for i in range(row, 0, -1):
        for k in range(i):
            print_star()

        for j in range(2*row - 2*i):
            print_space()

        for k in range(i):
            print_star()
        next_line()
            

row = int(input("Row Num: "))

butterfly(row)
