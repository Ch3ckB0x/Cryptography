alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar_cipher(encryption_text, shift):
    caesar_cipher_list = []
    for i in encryption_text:
        if i in alphabet:
            index = alphabet.index(i)
            index = int((index + shift) % 26)
            i = alphabet[index]
        elif i in ALPHABET:
            index = ALPHABET.index(i)
            index = int((index + shift) % 26)
            i = ALPHABET[index]
        else:
            i = i
        caesar_cipher_list += i
    caesar_cipher_text = "".join(caesar_cipher_list)
    return caesar_cipher_text

def all_shift():
    text = input("Enter text for decryption: ")
    shift = range(0, 26)
    for i in shift:
        shift = i
        cipher = caesar_cipher(text, shift)
        print(f"In Rot{i}: {cipher}")

if __name__ == "__main__":
    all_shift()