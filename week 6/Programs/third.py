def its_prime(number):
    if number<=1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
try:
    input_number=int(input("Enter an Integer: "))
    if input_number<0:
        print("Please enter a positive Integer.")
    elif its_prime(input_number):
        print(f"{input_number} is a prime number")
    else:
        print(f"{input_number} is not a prime number")
except ValueError:
    print("Invalid Input, re-try.")
