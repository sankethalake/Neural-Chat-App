import numpy as np

block_size_unpadded = 5
block_padding = 11
block_size = block_size_unpadded + block_padding

chrlist = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '!', '?',
    ':', ' '
]
binlist = [
    '00000', '00001', '00010', '00011', '00100', 
    '00101', '00110', '00111', '01000', '01001',
    '01010', '01011', '01100', '01101', '01110', 
    '01111', '10000', '10001', '10010', '10011',
    '10100', '10101', '10110', '10111', '11000',
    '11001', '11010', '11011', '11100', '11101', 
    '11110', '11111'
]

def randombits(n):
    if n == 0:
        return ''
    decvalue = np.random.randint(0, 2**n)
    formatstring = '0' + str(n) + 'b'
    return format(decvalue, formatstring)

def encstr(message, block_padding=0):
    cipher = ''
    bintext = ' '.join('{0:016b}'.format(ord(x), 'b') for x in message)
    cipher  = bintext.replace(" ", "")

    return [cipher, len(message)]

def decstr(cipher, n, block_padding=0):
    seperated = ''
    for i in range(len(cipher)):
        if i%16 == 0:
            seperated += " "
        seperated += cipher[i]

    # print(seperated)
    bin_list = seperated.split()
    text = ''

    for bin in bin_list:
        an_integer = int(bin, 2)
        ascii_character = chr(an_integer)
        text += ascii_character

    return text


def strToArr(bin_string,block_size):
    bin_list = []
    keys = []
    letter_count = 0
    innerList = []
    
    for letter in bin_string:
        innerList.append(int(letter))
        letter_count += 1
        if (letter_count % block_size) == 0:
            bin_list.append(innerList)
            innerList = []
            key_bit = np.random.randint(0, 2, 16)
            keys.append(key_bit)
    
    input_list = np.array(bin_list)
    key_list = np.array(keys)
    return [input_list, key_list]

def arrToStr(bin_arr):
    bin_string = ''
    
    for inner in bin_arr:
        for bit in inner:
            bin_string += str(bit)
    return bin_string