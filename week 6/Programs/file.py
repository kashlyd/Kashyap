import random
import string

def encrypt_with_interval(message):
    interval = random.randint(2, 20)
    encrypted_message = ''
    
    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char
            if i % interval == interval - 1:
                encrypted_message += random.choice(string.ascii_lowercase)

    return encrypted_message, interval

def decrypt_with_interval(encrypted_message, interval_used):
    decrypted_message = ''

    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            decrypted_message += char
            if (i + 1) % (interval_used + 1) == 0:
                # Skip the next random letter
                i += 1

    return decrypted_message

# Example usage:
try:
    input_message = input("Enter a message: ")
    encrypted_result, interval_used = encrypt_with_interval(input_message)
    print(f"Encrypted message: {encrypted_result}")
    print(f"Interval used: {interval_used}")

    decrypted_result = decrypt_with_interval(encrypted_result, interval_used)
    print(f"Decrypted message: {decrypted_result}")

except Exception as e:
    print(f"An error occurred: {e}")
