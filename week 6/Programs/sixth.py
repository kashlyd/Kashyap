def decrypt_with_interval(encrypted_message, interval_used):
    decrypted_message = ''
    random_letters = ''

    for char in encrypted_message:
        if char.isalpha():
            decrypted_message += char
        else:
            random_letters += char

    random_index = 0
    for i in range(len(decrypted_message)):
        if decrypted_message[i].isalpha() and random_index < len(random_letters):
            decrypted_message = decrypted_message[:i] + random_letters[random_index] + decrypted_message[i+1:]
            random_index += 1

    return decrypted_message

# Example usage:
try:
    input_message = input("Enter the encrypted message: ")
    interval_used = int(input("Enter the interval used: "))
    
    decrypted_result = decrypt_with_interval(input_message, interval_used)
    print(f"Decrypted message: {decrypted_result}")
except Exception as e:
    print(f"An error occurred: {e}")
