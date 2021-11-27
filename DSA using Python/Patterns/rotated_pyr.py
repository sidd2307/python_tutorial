print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")

def rotated_half_pyramid(row):
    for i in range(row):
        for j in range(row-i-1):
            print_space()
        for j in range(i+1):
            print_star()
        next_line()

row = int(input("Row Num: "))

rotated_half_pyramid(row)
