# --------------------------
# Name: Jiayao Pang ID:194174300
# CP460 (Fall 2019)
# Assignment 3
# --------------------------

import math
import string
import utilities_A3


# ---------------------------------
#  Q1: Columnar Transposition    #
# ---------------------------------
# -----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid columnar transposition key 
#               Returns key order, e.g. [face] --> [1,2,3,0]
#               Removes repetitions and non-alpha characters from key
#               If empty string or not a string -->
#                   print an error msg and return [0] (which is a)
#               Upper 'A' and lower 'a' are the same order
# -----------------------------------------------------------
def get_keyOrder_columnarTrans(key):
    # your code here
    # not string
    if not isinstance(key, str):
        print('Error: Invalid Columnar Transposition Key', end=' ')
        return [0]

    # invalid key type 1
    remove_nonalpha = ''
    for char in key:
        if char.isalpha():
            remove_nonalpha += char
    if len(remove_nonalpha) == 0:
        print('Error: Invalid Columnar Transposition Key', end=' ')
        return [0]

    # invalid key type 2
    remove_repetition = ''
    for c in remove_nonalpha.lower():
        if c not in remove_repetition:
            remove_repetition += c
    if len(remove_repetition) == 0:
        print('Error: Invalid Columnar Transposition Key', end=' ')
        return [0]

    # valid key
    tempOrder = []
    for k1 in remove_repetition:
        temp = 0
        for k2 in remove_repetition:
            if ord(k1.lower()) > ord(k2.lower()):
                temp += 1
        tempOrder.append(temp)

    keyOrder = []
    for i in range(len(remove_repetition)):
        keyOrder.append(tempOrder.index(i))

    return keyOrder


# -----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Columnar Transposition Cipher
# -----------------------------------------------------------
def e_columnarTrans(plaintext, key):
    # your code here
    key_order = get_keyOrder_columnarTrans(key)

    c = len(key_order)
    r = int(math.ceil(len(plaintext) / c))

    matrix = utilities_A3.new_matrix(r, c, '')

    counter = 0
    for i in range(r):
        for j in range(c):
            matrix[i][j] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter += 1

    ciphertext = ''
    for i in key_order:
        for j in range(r):
            ciphertext += matrix[j][i]

    return ciphertext


# -----------------------------------------------------------
# Parameters:   ciphertext (str)
#               kye (str)
# Return:       plaintext (list)
# Description:  Decryption using Columnar Transposition Cipher
# -----------------------------------------------------------
def d_columnarTrans(ciphertext, key):
    # your code here
    key_order = get_keyOrder_columnarTrans(key)

    c = len(key_order)
    r = int(math.ceil(len(ciphertext) / c))

    matrix = utilities_A3.new_matrix(r, c, '')

    blocks = utilities_A3.text_to_blocks(ciphertext, r)

    counter = 0
    for i in key_order:
        for j in range(r):
            matrix[j][i] = blocks[counter][j]
        counter += 1

    plaintext = ''
    for i in range(r):
        for j in range(c):
            plaintext += matrix[i][j]
    while plaintext[-1] == 'q':
        plaintext = plaintext[:-1]

    return plaintext


# ---------------------------------
#   Q2: Permutation Cipher       #
# ---------------------------------

# -----------------------------------------------------------
# Parameters:   plaintext (str)
#               key(key,mode)
# Return:       ciphertext (str)
# Description:  Encryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be used whenever necessary
# -----------------------------------------------------------
def e_permutation(plaintext, key):
    # your code here
    if not is_valid(key, 'e'):
        return ''

    if int(key[1]) == 0:
        temp_text = utilities_A3.get_lower()
        temp_key = ''
        for c in key[0]:
            temp_key += temp_text[int(c)]
        ciphertext = e_columnarTrans(plaintext, temp_key)

    else:
        blocks = utilities_A3.text_to_blocks(plaintext, len(key[0]))
        while len(blocks[-1]) != len(key[0]):
            blocks[-1] += 'q'
        ciphertext = ''
        for block in blocks:
            for i in key[0]:
                ciphertext += block[int(i) - 1]

    return ciphertext


# -----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key(key,mode)
# Return:       plaintext (str)
# Description:  Decryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be removed
# -----------------------------------------------------------
def d_permutation(ciphertext, key):
    # your code here
    if not is_valid(key, 'd'):
        return ''

    if int(key[1]) == 0:
        temp_text = utilities_A3.get_lower()
        temp_key = ''
        for c in key[0]:
            temp_key += temp_text[int(c)]
        plaintext = d_columnarTrans(ciphertext, temp_key)

    else:
        blocks = utilities_A3.text_to_blocks(ciphertext, len(key[0]))

        plaintext = ''
        inverse_sequence = []
        for i in range(len(key[0])):
            inverse_sequence.append(key[0].index(str(i + 1)))

        for block in blocks:
            for j in inverse_sequence:
                plaintext += block[j]
        while plaintext[-1] == 'q':
            plaintext = plaintext[:-1]

    return plaintext


# -------------------------------------------------------------------
# Parameters:   key (key,mode)
#               op (str) 'd' for decryption and 'e' for encryption
# Return:       True/False
# Description:  Check whether the key for permutation is valid or not
# -------------------------------------------------------------------
def is_valid(key, op):
    """
    if not isinstance(key, tuple):
        return False
    elif len(key) != 2:
        return False
    """
    if not str(key[0]).isnumeric():
        if op == 'e':
            print('Error (e_permutation): Invalid key')
        else:
            print('Error (d_permutation): Invalid key')
        return False
    else:
        remove_repetition = ''
        for c in key[0]:
            if c not in remove_repetition:
                remove_repetition += c
        if len(remove_repetition) < len(key[0]):
            if op == 'e':
                print('Error (e_permutation): Invalid key')
            else:
                print('Error (d_permutation): Invalid key')
            return False

        for i in range(len(key[0])):
            if str(i + 1) not in remove_repetition:
                if op == 'e':
                    print('Error (e_permutation): Invalid key')
                else:
                    print('Error (d_permutation): Invalid key')
                return False

    if int(key[1]) != 0 and int(key[1]) != 1:
        if op == 'e':
            print('Error (e_permutation): Invalid mode')
        else:
            print('Error (d_permutation): Invalid mode')
        return False

    return True


# ---------------------------------
#       Q3: ADFGVX Cipher        #
# ---------------------------------
# --------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using ADFGVX cipher
# --------------------------------------------------------------
def e_adfgvx(plaintext, key):
    # your code here
    ciphertext = ''
    square = utilities_A3.get_adfgvx_square()
    base_string = 'ADFGVX'

    for p in plaintext:
        index = utilities_A3.index_matrix(p.upper(), square)
        if index[0] != -1:
            ciphertext += base_string[index[0]] if p.isupper() else base_string[index[0]].lower()
            ciphertext += base_string[index[1]] if p.isupper() else base_string[index[1]].lower()
        else:
            ciphertext += p

    ciphertext = e_columnarTrans(ciphertext, key)

    return ciphertext


# --------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using ADFGVX cipher
# --------------------------------------------------------------
def d_adfgvx(ciphertext, key):
    # your code here
    ciphertext = d_columnarTrans(ciphertext, key)

    square = utilities_A3.get_adfgvx_square()
    base_string = 'ADFGVX'

    plaintext = ''
    counter = 0
    while counter < len(ciphertext):
        if ciphertext[counter].upper() in base_string:
            r = base_string.index(ciphertext[counter].upper())
            c = base_string.index(ciphertext[counter + 1].upper())
            tempChar = square[r][c]
            plaintext += tempChar if ciphertext[counter].isupper() else tempChar.lower()
            counter += 2

        else:
            plaintext += ciphertext[counter]
            counter += 1

    return plaintext


# ---------------------------------
#       Q4: One Time Pad         #
# ---------------------------------
# --------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using One Time Pad
#               Result is shifted by 32
# --------------------------------------------------------------
def e_otp(plaintext, key):
    # your code here
    temp = plaintext.replace('\n', '')
    if len(temp) != len(key):
        print('Error (e_otp): Invalid key')
        return ''

    ciphertext = ''
    counter = 0
    for p in plaintext:
        if p == '\n':
            ciphertext += '\n'
        else:
            ascii_num = ord(xor_otp(p, key[counter])) + 32
            ciphertext += chr(ascii_num)
            counter += 1

    return ciphertext


# --------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using One Time Pad
#               Input is shifted by 32
# --------------------------------------------------------------
def d_otp(ciphertext, key):
    # your code here
    temp = ciphertext.replace('\n', '')
    if len(temp) != len(key):
        print('Error (d_otp): Invalid key')
        return ''

    plaintext = ''
    counter = 0
    for c in ciphertext:
        if c == '\n':
            plaintext += '\n'
        else:
            ascii_char = chr(ord(c) - 32)
            plaintext += xor_otp(ascii_char, key[counter])
            counter += 1

    return plaintext


# --------------------------------------------------------------
# Parameters:   char1 (str)
#               char2 (str)
# Return:       result (str)
# Description:  Takes two characters. Convert their corresponding
#               ASCII value into binary (8-bits), then performs xor
#               operation. The result is treated as an ASCII value
#               which is converted to a character
# --------------------------------------------------------------
def xor_otp(char1, char2):
    # your code here
    v1 = ord(char1)
    v2 = ord(char2)

    xor = v1 ^ v2

    result = chr(xor)

    return result


# ---------------------------------
#    Q5: Myszkowski Cipher      #
# ---------------------------------
# -----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid Myszkowski key 
#               Returns key order, e.g. [meeting] --> [3,0,0,5,2,4,1]
#               The key should have some characters that are repeated
#               and some characters that are non-repeated. 
#               if invalid key --> return [1,1,0]
#               Upper and lower case characters are considered of same order
#               non-alpha characters sould be ignored
# -----------------------------------------------------------
def get_keyOrder_myszkowski(key):
    # your code here
    # invalid key type 1
    if not isinstance(key, str):
        print('Error: Invalid Myszkowski Key', end=' ')
        return [1, 1, 0]
    # invalid key type 2
    if len(key) == 0:
        print('Error: Invalid Myszkowski Key', end=' ')
        return [1, 1, 0]
    # invalid key type 3 & 4
    remove_nonalpha = ''
    for char in key:
        if char.isalpha():
            remove_nonalpha += char
    if len(remove_nonalpha) == 0:
        print('Error: Invalid Myszkowski Key', end=' ')
        return [1, 1, 0]

    remove_repetition = ''
    for c in remove_nonalpha.lower():
        if c not in remove_repetition:
            remove_repetition += c
    if len(remove_repetition) == len(key) or len(remove_repetition) == len(key) / 2:
        print('Error: Invalid Myszkowski Key', end=' ')
        return [1, 1, 0]

    # valid key
    keyOrder = []
    for k1 in remove_nonalpha:
        temp = 0
        for k2 in remove_nonalpha:
            if ord(k1.lower()) > ord(k2.lower()):
                temp += 1
        keyOrder.append(temp)

    str_keyOrder = ''
    for order in keyOrder:
        str_keyOrder += str(order)

    for i in range(len(remove_repetition)):
        if str(i) not in str_keyOrder:
            for j in range(i, len(remove_nonalpha)):
                if str(j) in str_keyOrder:
                    str_keyOrder = str_keyOrder.replace(str(j), str(j - (j - i)))
                    break

    keyOrder = []
    for key in str_keyOrder:
        keyOrder.append(int(key))

    return keyOrder


# --------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Myszkowsi Transposition
# --------------------------------------------------------------
def e_myszkowski(plaintext, key):
    # your code here
    key_order = get_keyOrder_myszkowski(key)
    ciphertext = ''

    c = len(key_order)
    r = int(math.ceil(len(plaintext) / c))

    matrix = utilities_A3.new_matrix(r, c, '')

    counter = 0
    for i in range(r):
        for j in range(c):
            matrix[i][j] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter += 1

    for i in range(c):
        for j in range(r):
            Index = 0
            while i in key_order[Index:c]:
                Index = key_order.index(i, Index, c)
                ciphertext += matrix[j][Index]
                Index += 1

    return ciphertext


# --------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Myszkowsi Transposition
# --------------------------------------------------------------
def d_myszkowski(ciphertext, key):
    # your code here
    return plaintext


