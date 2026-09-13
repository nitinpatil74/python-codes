#Check If a Given Number Is a Prime Number
#A prime number is any positive non-zero number that is only divisible by itself or by 1.

#For example, 11 is a prime number.

#To create a Python program that finds if a number is a prime number, you need to:

#Have a target number.
#Ensure the number is more than 1.
#Loop through all the numbers that are less than half the target number.
#Check if any number divides the target evenly.
#For example, to check if 11 is a prime number, you need to check if any of the following numbers divides it evenly: 2, 3, 4, 5.

#Here is a Python program that checks if a given number is a prime number:
def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                break
        else:
            print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        
is_prime(11)
is_prime(7)
is_prime(16)