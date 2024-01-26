def frequency_analysis(message):
    letter_counts = {}

    for char in message:
        if char.isalpha():
            char_lower = char.lower()  # Convert to lowercase to make case-insensitive
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1

    # Sort the letters by frequency in descending order
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their counts
    print("Six most common letters and their counts:")
    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count}")

# Example:
try:
    input_message = input("Enter the message: ")
    frequency_analysis(input_message)
except Exception as e:
    print(f"An error occurred: {e}")
