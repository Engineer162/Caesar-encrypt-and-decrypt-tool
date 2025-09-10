# Ceasar cipher encrypt and ecrypt tool written in Python, in part by Engineer162.

alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Function for shifting a character by a given integer
def shiftcharacter(k,i):
    p = alfabet.index(k)
    if p + i >= 26:
        p = p - 26
    return alfabet[p + i]

# Function for encrypting text. expects an integer and a string as input
def encrypttext(i, txt):
    ciphertext = ""
    for k in txt:
        if k in alfabet:
            ciphertext += shiftcharacter(k, i)
        else:
            ciphertext += k
    return ciphertext

# Function for decrypting text. expects an integer and a string as input
def decrypttext(i, txt):
    cleartext = ""
    for k in txt:
        if k in alfabet:
            cleartext += shiftcharacter(k, -i)
        else:
            cleartext += k
    return cleartext

# Main menu
print("Choose a function:")
print("1. Encrypt text")
print("2. Dekrypt text")

# User input for main menu choice
choice = input("Submit your choice (1/2): ")

# If the choice is 1, encrypt text.
if choice == "1":
    cleartext = input("Input unencrypted text: ").upper()
    i = int(input("Input shift ammount (integer): "))
    print("Encrypted text:", encrypttext(i, cleartext))

# If the choice is 2, decrypt text.
elif choice == "2":
    ciphertext = input("Input encrypted text: ").upper()
    i = int(input("Input shift ammount (integer): "))
    print("Decrypted text:", decrypttext(i, ciphertext))

# If the choice is neither 1 nor 2, print an error message.
else:
    print("Invalid choice.")