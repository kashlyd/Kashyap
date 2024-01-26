import random
import string

def encrypt_with_interval(message):
    interval = random.randint(2, 20)

    random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(interval - 1))

    encrypted_message = ''
    random_index = 0
    for char in message:
        if char.isalpha():
            encrypted_message += char
            if random_index < len(random_letters):
                encrypted_message += random_letters[random_index]
                random_index += 1

    return encrypted_message, interval

# Example usage:
try:
    input_message = input("Enter a message: ")
    encrypted_result, interval_used = encrypt_with_interval(input_message)
    print(f"Encrypted message: {encrypted_result}")
    print(f"Interval used: {interval_used}")
except Exception as e:
    print(f"An error occurred: {e}")
