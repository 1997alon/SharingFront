import json


# ASCII conversion function
def ascii_encrypt(message):
    encrypted_message = ' '.join(str(ord(c)) for c in message)
    # Append null character (ASCII value 0) at the end of the message
    encrypted_message += " \0"
    return encrypted_message


def ascii_decrypt(encrypted_message):
    encrypted_message = encrypted_message.strip().split(' ')

    # Remove the null character (ASCII value 0) which is added during encryption
    encrypted_message = encrypted_message[:-1]

    # Convert the ASCII values back to characters
    decrypted_message = ''.join(chr(int(c)) for c in encrypted_message)

    return decrypted_message