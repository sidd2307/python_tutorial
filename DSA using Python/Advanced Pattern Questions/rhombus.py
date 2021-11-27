print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end=" ")

def rhombus(row):
    for i in range(row):
        for j in range(row-i-1):
            print_space()
        for j in range(row):
            print_star()
        next_line()            

row = int(input("Row Num: "))

rhombus(row)
