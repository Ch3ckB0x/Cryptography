#--------------------------------------------
# Program by Lotonina.G.
#
#
# Version     Data          Info
#   1.0       2020     Initial Version
#
#--------------------------------------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def atbash_cipher(text):
    atbash_cipher_list = []
    for i in text:
        if i in alphabet:
            i = alphabet[len(alphabet) - alphabet.index(i) - 1]
        elif i in ALPHABET:
            i = ALPHABET[len(alphabet) - alphabet.index(i) - 1]
        else:
            i = i
        atbash_cipher_list += i
    atbash_cipher_text = "".join(atbash_cipher_list)
    print(atbash_cipher_text)
    return atbash_cipher_text


if __name__ == "__main__":
    text = input("Enter text for decryption: ")
    atbash_cipher(text)