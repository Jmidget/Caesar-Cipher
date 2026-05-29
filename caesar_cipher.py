import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(mode, text, shift):
    word = ''
    for letter in text:
        if alphabet.count(letter) == 1:
            if mode == 'encode':
                position = alphabet.index(letter) + shift
            elif mode == 'decode':
                position = alphabet.index(letter) - shift
            if 0 < position < 26:
                word += alphabet[position]
            elif position >= 26:
                position = position % 26
                word += alphabet[position]
            elif position < 0:
                position = -(abs(position) % 26)
                word += alphabet[position]
        elif alphabet.count(letter) == 0:
            word += letter
    print(f'Here is the {mode}d result: {word}')

caesar_cipher_on = True
while caesar_cipher_on:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(mode, text, shift)
    if (input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")).lower() == 'no':
        caesar_cipher_on = False
    else:
        continue