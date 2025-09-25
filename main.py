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
mode = input("Would you like to encrypt or decrypt? ").strip().lower()
key = input("Please enter your key (1-25): ").strip()

if mode == "encrypt":
    plaintext = input("Please enter your plaintext below:\n")
    encrypted_message = ""
    for character in plaintext:
        if character in special_characters:
            encrypted_message += character
        else:
            # Store encrypted_character value
            encrypted_value = alphabet.get(character) + int(key)
            # Convert encrypted_character value to key
            for k, v in alphabet.items():
                if v == encrypted_value:
                    encrypted_character = k
                    break
            encrypted_message += encrypted_character
    print(f"Your message has been encrypted:\n{encrypted_message}")        