print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")

def half_inverted_pyramid(row):
    for i in range(row, 0, -1):
        for j in range(i):
            print_star()
        next_line()

row = int(input("Row Num: "))

half_inverted_pyramid(row)
