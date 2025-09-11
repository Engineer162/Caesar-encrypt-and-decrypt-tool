# Caesar + Substitution hybrid cipher written in Python, in part by Engineer162.

# Define the alphabet (Danish)
alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Define a substitution key (can be randomized using shuffle.py)
key = ['D','M','T','P','Z','L','S','A','W','O','C','N','V','X','R','I','K','G','F','U','H','E','Q','J','B','Y']

# Function for shifting a character by a given integer
def shiftcharacter(k,i):
    p = alfabet.index(k)
    if p + i >= 26:
        p = p - 26
    return alfabet[p + i]

# Function for encrypting text. expects an integer and a string as input
def caesar_encrypt(i, txt):
    result = ""
    for k in txt:
        if k in alfabet:
            result += shiftcharacter(k, i)
        else:
            result += k
    return result

# Function for decrypting text. expects an integer and a string as input
def caesar_decrypt(i, txt):
    result = ""
    for k in txt:
        if k in alfabet:
            result += shiftcharacter(k, -i)
        else:
            result += k
    return result

# Function for encrypting the text again using substitution cipher
def substitution_encrypt(txt):
    result = ""
    for k in txt:
        if k in alfabet:
            idx = alfabet.index(k)
            result += key[idx]
        else:
            result += k
    return result

# Function for decrypting the text using substitution cipher
def substitution_decrypt(txt):
    result = ""
    for k in txt:
        if k in key:
            idx = key.index(k)
            result += alfabet[idx]
        else:
            result += k
    return result

# Function combining both encryption methods
def dualencrypt(i, txt):
    step1 = caesar_encrypt(i, txt)
    step2 = substitution_encrypt(step1)
    return step2

# Function combining both decryption methods
def dualdecrypt(i, txt):
    step1 = substitution_decrypt(txt)
    step2 = caesar_decrypt(i, step1)
    return step2

# Main menu
print("Choose a function:")
print("1. Encrypt text (Using both Caesar + Substitution)")
print("2. Decrypt text (Using both Caesar + Substitution)")

# User input for main menu choice
choice = input("Submit your choice (1/2): ")

# If the choice is 1, encrypt text.
if choice == "1":
    cleartext = input("Input unencrypted text: ").upper()
    i = int(input("Input shift amount (integer): "))
    print("Encrypted text:", dualencrypt(i, cleartext))

# If the choice is 2, decrypt text.
elif choice == "2":
    ciphertext = input("Input encrypted text: ").upper()
    i = int(input("Input shift amount (integer): "))
    print("Decrypted text:", dualdecrypt(i, ciphertext))

# If the choice is neither 1 nor 2, print an error message.
else:
    print("Invalid choice.")
