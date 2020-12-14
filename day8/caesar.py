from typing import cast


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = input("Type 'encode' to encrypt and 'decode' to decrypt.\n")
message = input("Type your message here.\n").lower()
shift = int(input("What is the shift?\n"))


def caesar(method, message, shift_amount):

    end_text = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        if method == 'decode':
        	new_position = (position - shift_amount) % 26
        new_letter = alphabet[new_position]
        end_text += new_letter
    return end_text

print(caesar(method, message, shift))
