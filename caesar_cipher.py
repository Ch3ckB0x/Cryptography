alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# caesar_cipher_encryption
def caesar_cipher_encryption(encryption_text):
    caesar_cipher_list = []
    for i in encryption_text:
        if i in alphabet:
            index = alphabet.index(i)
            index = int((index + shift) % 26)
            i = alphabet[index]
            caesar_cipher_list += i
        elif i in ALPHABET:
            index = ALPHABET.index(i)
            index = int((index + shift) % 25)
            i = ALPHABET[index]
            caesar_cipher_list += i
        else:
            i = i
            caesar_cipher_list += i
    caesar_cipher_text = "".join(caesar_cipher_list)
    return caesar_cipher_text


encryption_text = input("Enter text for encryption: ")
shift = int(input("Enter shift(0-25): "))

encrypter = caesar_cipher_encryption(encryption_text)
print(encrypter)