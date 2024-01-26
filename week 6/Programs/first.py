def decimal_to_binary(number):
    return bin(number)[2:] if isinstance(number, int) and number >= 0 else None

try:
    positive_integer = int(input("Enter a positive integer: "))
    binary_representation = decimal_to_binary(positive_integer)
    if binary_representation is not None:
        print(f"The binary representation of {positive_integer} is: {binary_representation}")
    else:
        print("Invalid input. Please enter a valid positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
