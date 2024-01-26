def unique_letters_sorted(input_string):
    # Create a set of unique lowercase letters from the input string
    unique_letters_set = set()
    for char in input_string:
        if char.isalpha():
            unique_letters_set.add(char.lower())
    
    # Sort the set and convert it to a list
    sorted_unique_letters = sorted(unique_letters_set)
    
    return sorted_unique_letters

# Test the function
try:
    input_string = input("Enter a string: ")
    result = unique_letters_sorted(input_string)
    print(f"Unique letters: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
