print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end="")

def inverted_pattern(row):
    for i in range(row, 0, -1):
        num = 1
        for j in range(i):
            print_char(num)
            num += 1
        next_line()
            

row = int(input("Row Num: "))

inverted_pattern(row)
