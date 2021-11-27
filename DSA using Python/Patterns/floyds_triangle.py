print_star = lambda : print("* ", end="")
print_space = lambda : print("  ", end="")
next_line = lambda : print("\n", end="")
print_char = lambda a : print(a, end=" ")

def floyds_triangle(row):
    count = 1;
    for i in range(row):
        for j in range(i+1):
            print_char(count)
            count += 1;
        next_line()
            

row = int(input("Row Num: "))

floyds_triangle(row)
