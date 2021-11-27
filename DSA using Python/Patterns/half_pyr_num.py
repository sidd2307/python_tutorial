print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end="")

def half_pyramid_numbers(row):
    for i in range(row):
        for j in range(i+1):
            print_char(i+1)
        next_line()
            

row = int(input("Row Num: "))

half_pyramid_numbers(row)
