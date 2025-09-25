alphabet = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
}
special_characters = [
    ' ',
    '.',
    ',',
    '!',
    '?',
    ';',
    ':',
]

active = True
while active:
    mode = input("\nWould you like to encrypt or decrypt?\n").strip().lower()
    key = input("Please enter your key (1-25): ").strip()
    if mode == "encrypt":
        plaintext = input("Please enter your plaintext below:\n").lower()
        encrypted_message = ""
        for character in plaintext:
            if character in special_characters:
                encrypted_message += character
            else:
                encrypted_value = alphabet.get(character) + int(key)
                # Catch wrapping values
                if encrypted_value >= 26:
                    encrypted_value -= 26
                elif encrypted_value <= -1:
                    encrypted_value += 26
                # Convert encrypted_value to corresponding character
                for k, v in alphabet.items():
                    if v == encrypted_value:
                        encrypted_character = k
                        break                
                encrypted_message += encrypted_character
        print(f"\nYour message has been encrypted:\n{encrypted_message}")
    elif mode == "decrypt":
        ciphertext = input("Please enter your ciphertext below:\n").lower()
        decrypted_message = ""
        for character in ciphertext:
            if character in special_characters:
                decrypted_message += character
            else:
                decrypted_value = alphabet.get(character) - int(key)
                # Catch wrapping values
                if decrypted_value >= 26:
                    decrypted_value -= 26
                elif decrypted_value <= -1:
                    decrypted_value += 26
                # Convert decrypted_value to corresponding character
                for k, v in alphabet.items():
                    if v == decrypted_value:
                        decrypted_character = k
                        break
                decrypted_message += decrypted_character
        print(f"\nYour message has been decrypted:\n{decrypted_message}")
    
    again = input("Continue (y/n)? ").strip().lower()
    if again == 'n':
        active = False