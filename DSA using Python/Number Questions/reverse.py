import math

print_mod = lambda a : print(a, end="")

def reverse(num):
    result = 0
    while(num > 0):
        data = num % 10
        result = result*10 + data
        num = num//10
    return result

num = int(input("Num: "))

print("The reverse of the number {} is {}".format(num, reverse(num)))
