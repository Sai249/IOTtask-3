def encrypt(text, shift):  #function named encrypt that takes two parameters: text and shift
    result = ""           #Initializes an empty string result to store the encrypted message.

    for i in range(len(text)):
        char = text[i]
        if char.isupper(): #Checks if the character char is a lowercase letter (a-z).

            result += chr((ord(char) + shift - 65) % 26 + 65) #Converts the character char to its ASCII value. For example, ord('a') is 97.
                                                               #Adds the shift value to the ASCII value of the character.

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97) # Subtracts 97 to normalize the ASCII value to a range starting from 0 
        else:
            result += char  #(ord(char) + shift - 97) % 26: Uses the modulo operator to wrap around the alphabet if the shift goes past ‘z’. This ensures the result stays within the range of 0-25.
                        #(ord(char) + shift - 97) % 26 + 97: Adds 97 back to convert the normalized value back to the ASCII range for lowercase letters.
                        #chr(…): Converts the final ASCII value back to a character.
                        #result += chr(…): Appends the encrypted character to the result string.
    return result

def decrypt(text, shift): # This line defines a function named decrypt that takes two parameters: text and shift .

    return encrypt(text, -shift) #Calls the encrypt function with the negative of the shift value to reverse the encryption process.

# Taking input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypting and decrypting the message
encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
