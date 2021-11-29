def is_armstrong(num):
    sum = 0
    original_number = num
    while(num != 0):
        rem = num%10
        sum += rem**3
        num = num//10
    if (sum == original_number):
        return True
    else:
        return False

num = int(input("Num: "))

if(is_armstrong(num)):
    print("Yes {} is an armstrong number!")
else:
    print("No {} is not an armstrong number!")