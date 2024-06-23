# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Shift character by specified number of places
            shifted = ord(char) + shift
            
            # Handle uppercase letters
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            
            # Handle lowercase letters
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            
            # Append encrypted character to ciphertext
            ciphertext += chr(shifted)
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift character by specified number of places in reverse
            shifted = ord(char) - shift
            
            # Handle uppercase letters
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            
            # Handle lowercase letters
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            
            # Append decrypted character to plaintext
            plaintext += chr(shifted)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    
    return plaintext

# Example usage:
def main():
    plaintext = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value (positive integer): "))
    
    encrypted_message = caesar_cipher_encrypt(plaintext, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
