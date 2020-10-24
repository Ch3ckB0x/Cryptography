alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
shift = 13

def caesar_cipher_encryption(encryption_text, shift):
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

def caesar_cipher_decryption(decryption_text, shift):
    caesar_cipher_list = []
    for i in decryption_text:
        if i in alphabet:
            index = alphabet.index(i)
            index = int((index - shift) % 26)
            i = alphabet[index]
            caesar_cipher_list += i
        elif i in ALPHABET:
            index = ALPHABET.index(i)
            index = int((index - shift) % 25)
            i = ALPHABET[index]
            caesar_cipher_list += i
        else:
            i = i
            caesar_cipher_list += i
    caesar_cipher_text = "".join(caesar_cipher_list)
    return caesar_cipher_text


def all_shift(cipher):
    if cipher == "d":
        text = input("Enter text for decryption: ")
        function = caesar_cipher_decryption
        print("I decoded your text")
    elif cipher == "e":
        text = input("Enter text for encryption: ")
        function = caesar_cipher_encryption
        print("I encoded your text")
    cipher = function(text, shift)
    print(f"In Rot13: {cipher}")

if __name__ == "__main__":
    all_shift(cipher = input("Encrypted(e) or Decrypted(d)?\n"))