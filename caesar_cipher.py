# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-3: What happens if you try to shift z forwards by 9? Can you fix the code?
# TODO-4: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# TODO-5: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-6: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-7: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
# TODO-8: Import and print the logo from art.py when the program starts.
# TODO-9: What happens if the user enters a number/symbol/space?
# TODO-10: Can you figure out a way to restart the cipher program?

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

