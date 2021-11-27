print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end=" ")

def check(i, j):
    if (i+j) % 2 == 0:
        return 1
    return 0

def zero_to_one(row):
    num = 1
    for i in range(row):
        for j in range(i+1):
            print_char(check(i, j))
        next_line()
            

row = int(input("Row Num: "))

zero_to_one(row)
