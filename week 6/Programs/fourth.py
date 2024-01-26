def simple_encrypt(message):
    encrypted_message = ''.join(message.split())[::-1]
    return encrypted_message

try:
    input_message = input("Enter message: ")
    encrypted_result = simple_encrypt(input_message)
    print(f"Encrypted message: {encrypted_result}")
except Exception as e:
    print(f"An error occurred: {e}")
