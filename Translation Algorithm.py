
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def translate(string):
    current_char = 0
    char = " "
    while current_char < len(string):
        alphabet_num = alphabet.index(char.lower())
        print(alphabet[alphabet_num + 1])
        current_char += 1
        char = string[current_char]


def translate_tester(string):
    current_char = 0
    while current_char < len(string):
        char = string[current_char]
        print(string[current_char])
        print(alphabet.index(char.lower()))
        print(alphabet[alphabet.index(char.lower()) + 2])
        current_char += 1
translate_tester("Bruh momentum")

