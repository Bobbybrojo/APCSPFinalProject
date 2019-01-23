
# alphabet list for functions to grab from
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            # second set for offsets up to 26 from z key
            ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define global variables and prompt user
global key
global phrase
key = input("What is your offset key for encryption/decryption? (A Number 0-26): ")
option = input("Would you like to encrypt or decrypt?(Enter E/D): ")
phrase = input("Enter the phrase you would like to be encrypted/decrypted: ")


# encrypt
def encrypt(string):
    current_char = 0
    print("Your encrypted code for " + string + " is: ")
    while current_char < len(string):
        char = string[current_char]

        print(alphabet[alphabet.index(char.lower()) + int(key)])
        current_char += 1


# decrypt
def decrypt(string):
    current_char = 0
    print("Your decrypted code for " + string + " is: ")
    while current_char < len(string):
        char = string[current_char]

        print(alphabet[alphabet.index(char.lower()) - int(key)])
        current_char += 1


# decrypt or encrypt based on user input
if option.lower() == "e":
    encrypt(phrase)
elif option.lower() == "d":
    decrypt(phrase)
else:
    print("You did not properly enter either 'e' or 'd' to encrypt or decrypt")

