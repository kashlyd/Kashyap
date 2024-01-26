def find_factors(number):
    factors =[]
    for i in range(1,number+1):
        if number%i==0:
            factors.append(i)
    return factors

try:
    input_number=int(input("Enter an Integer: "))
    if input_number<=0:
        print("Please enter a postitive integer: ")
    else:
        result_factors=find_factors(input_number)
        print(f"The factors of {input_number} are {result_factors}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")