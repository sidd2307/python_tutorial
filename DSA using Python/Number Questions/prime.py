import math

print_mod = lambda a : print(a, end="")

def prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

num = int(input("Num: "))

if prime(num):
    print_mod("Prime Number")
else:
    print_mod("Not a Prime Number")
