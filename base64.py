#--------------------------------------------
# Program by Lotonina.G.
#
#
# Version     Data          Info
#   1.0       2020     Initial Version
#
#--------------------------------------------
base64_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

ascii = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*',
         43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5',
         54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@',
         65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K',
         76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V',
         87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a',
         98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k',
         108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u',
         118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~'}


# main function
def base64_cipher_encoding(text):
    list_for_dec = []
    list_for_all_bin = []
    # text in dec
    for i in text:
        dec_i = list(ascii.keys())[list(ascii.values()).index(i)]
        list_for_dec.append(dec_i)
    # dec to binary
    for dec in list_for_dec:
        binary = dec_to_bin(dec)
        for bin in binary:
            list_for_all_bin.append(bin)
    while len(list_for_all_bin) % 6 != 0:
        list_for_all_bin.append(0)
    # dec to base64
    list_base64 = bin_to_dec_for_base64(list_for_all_bin)
    if len(text) % 3 == 0:
        pass
    elif len(text) % 3 == 1:
        list_base64.append('==')
    elif len(text) % 3 == 2:
        list_base64.append('=')
    list_base64_in_text = ''.join(list_base64)
    return list_base64_in_text



def dec_to_bin(dec):
    list_for_bin = []
    all_dec_in_bin = []
    # Цикл перевода из 10 в 2 сист. счисл.
    while True:
        list_for_bin.append(dec % 2)
        dec = dec // 2
        if dec == 1:
            list_for_bin.append(1)
            while len(list_for_bin) != 8:
                list_for_bin.append(0)
            # правильно
            list_for_bin.reverse()
            break
    for bin in list_for_bin:
        all_dec_in_bin.append(bin)
    return all_dec_in_bin


def bin_to_dec_for_base64(list_for_all_bin):
    list_base64 = []
    end = len(list_for_all_bin) // 6
    for i in range(0, end):
        list_for_convert_to_dec = (list_for_all_bin[i*6: i*6+6])
        str_bin = ''.join(map(str, list_for_convert_to_dec))
        dec = bin_to_dec(str_bin)
        list_base64.append(base64_symbols[dec])
    return list_base64


def bin_to_dec(str_bin):
    str_bin_reverse = str_bin[::-1]
    dec = 0
    for i in enumerate(str_bin_reverse):
        dec += int(i[1]) * 2 ** i[0]
    return dec


if __name__ == '__main__':
    text = input('Enter text for base64 encryption: ')
    base64_encryption = base64_cipher_encoding(text)
    print(base64_encryption)