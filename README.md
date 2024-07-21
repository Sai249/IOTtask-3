1. Encrypt Function

   def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
-def encrypt(text, shift): This line defines a function named encrypt that takes two parameters: text (the message to be encrypted) and shift (the number of positions to shift each letter).
-result = “”: Initializes an empty string result to store the encrypted message.
-for i in range(len(text)): Loops through each character in the text.
-char = text[i]: Gets the current character from the text.
-if char.isupper(): Checks if the character is an uppercase letter.
  -result += chr((ord(char) + shift - 65) % 26 + 65): Shifts the character by the shift value and wraps around if necessary, then appends it to result.
-elif char.islower(): Checks if the character is a lowercase letter.
   -result += chr((ord(char) + shift - 97) % 26 + 97): Shifts the character by the shift value and wraps around if necessary, then appends it to result.
-else: If the character is neither uppercase nor lowercase (e.g., a space or punctuation), it is added to result without any change.
-return result: Returns the encrypted message.
2. Decrypt Function
- def decrypt(text, shift): This line defines a function named decrypt that takes two parameters: text (the message to be decrypted) and shift (the number of positions to shift each letter back).
-return encrypt(text, -shift): Calls the encrypt function with the negative of the shift value to reverse the encryption process.

3. User Input and Main Logic

# Taking input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypting and decrypting the message
encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")


Uppercase Letters

if char.isupper():
    result += chr((ord(char) + shift - 65) % 26 + 65)
    
-char.isupper(): Checks if the character char is an uppercase letter (A-Z).
-ord(char): Converts the character char to its ASCII value. For example, ord('A') is 65.
-ord(char) + shift: Adds the shift value to the ASCII value of the character.
-ord(char) + shift - 65: Subtracts 65 to normalize the ASCII value to a range starting from 0 (i.e., ‘A’ becomes 0, ‘B’ becomes 1, etc.).
-(ord(char) + shift - 65) % 26: Uses the modulo operator to wrap around the alphabet if the shift goes past ‘Z’. This ensures the result stays within the range of 0-25.
-(ord(char) + shift - 65) % 26 + 65: Adds 65 back to convert the normalized value back to the ASCII range for uppercase letters.
-chr(…): Converts the final ASCII value back to a character.
-result += chr(…): Appends the encrypted character to the result string.

Lowercase Letters

elif char.islower():
    result += chr((ord(char) + shift - 97) % 26 + 97)
-char.islower(): Checks if the character char is a lowercase letter (a-z).
-ord(char): Converts the character char to its ASCII value. For example, ord('a') is 97.
-ord(char) + shift: Adds the shift value to the ASCII value of the character.
-ord(char) + shift - 97: Subtracts 97 to normalize the ASCII value to a range starting from 0 (i.e., ‘a’ becomes 0, ‘b’ becomes 1, etc.).
-(ord(char) + shift - 97) % 26: Uses the modulo operator to wrap around the alphabet if the shift goes past ‘z’. This ensures the result stays within the range of 0-25.
-(ord(char) + shift - 97) % 26 + 97: Adds 97 back to convert the normalized value back to the ASCII range for lowercase letters.
-chr(…): Converts the final ASCII value back to a character.
-result += chr(…): Appends the encrypted character to the result string.

Non-Alphabetic Characters
else:
    result += char
    If the character is neither uppercase nor lowercase (e.g., a space, punctuation, or number), it is added to the result string without any change.
This ensures that only alphabetic characters are shifted, while other characters remain unchanged.
