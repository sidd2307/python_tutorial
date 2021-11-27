print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")

def hollow_rect(row, col):
    for i in range(col):
        print_star()
    print("\n")
    
    for i in range(row-2):
        print_star()
        for j in range(col-2):
            print_space()
        print_star()
        print("\n")


    for i in range(col):
        print_star()
    print("\n")

row = int(input("Row Num: "))
col = int(input("Col Num: "))

hollow_rect(row, col)
