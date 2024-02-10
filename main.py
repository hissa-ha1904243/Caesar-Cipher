import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_num):
    cipher_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        position = position + shift_num
        new_char = alphabet[position % len(alphabet)]
        cipher_text += new_char
    print(cipher_text)


def decrypt(cipher_text, shift_num):
    plain_text = ""
    for char in cipher_text:
        position = alphabet.index(char)
        position = position - shift_num
        new_char = alphabet[position % len(alphabet)]
        plain_text += new_char
    print(plain_text)


print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(text, shift)
    elif direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(text, shift)
    else:
            print("Invalid Choice!")
    restart = input("Do you want to restart? Type 'yes' or 'No':\n").lower()
    if restart == "no":
        print("Good Bye")
        break


