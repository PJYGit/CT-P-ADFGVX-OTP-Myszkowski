# --------------------------
# CP460 (Fall 2019)
# Assignment 3 Testing File
# --------------------------

import solution_A3
import utilities_A3


# ----------------------------------------------------
# Test Q1: Columnar Transposition
# ---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print("Testing Q1: Columnar Transposition")
    print()

    print('Testing get_keyOrder_columnarTrans:')
    keys = [34, ['O', 'N'], '', '034', '?=!', 'r', 'K', 'Dad', 'Face', 'apple', 'good day', 'German']
    for key in keys:
        print('Key order for {} ='.format(key), end=' ')
        keyOrder = solution_A3.get_keyOrder_columnarTrans(key)
        print(keyOrder)

    print()
    print('Testing Encryption/Decryption:')
    key = 'German'
    print('key = ', key)
    plaintext = 'DEFENDEASTERNWALLOFTHECASTLE'
    print('plaintext =  ', plaintext)
    ciphertext = solution_A3.e_columnarTrans(plaintext, key)
    print('ciphertext = ', ciphertext)
    plaintext2 = solution_A3.d_columnarTrans(ciphertext, key)
    print('plaintext2 = ', plaintext2)
    print()

    key = 'Truth Seeker'
    print('key = ', key)
    print('Key order = {}'.format(solution_A3.get_keyOrder_columnarTrans(key)))
    print('plaintext1 =')
    plaintext = utilities_A3.file_to_text('plaintext1.txt')
    print(plaintext[:103])
    ciphertext = solution_A3.e_columnarTrans(plaintext, key)
    print('ciphertext = ')
    print(ciphertext[:103])
    plaintext2 = solution_A3.d_columnarTrans(ciphertext, key)
    print('plaintext2 = ')
    print(plaintext2[:103])
    print("-------------------------------------------")
    print()
    return


# ----------------------------------------------------
# Test Q2: Permutation Cipher
# ---------------------------------------------------
def test_q2():
    print("-------------------------------------------")
    print("Testing Q2: Permutation Cipher")
    print()

    key = '7356412'
    print('key = ', key)
    plaintext = 'Love is blind. Friendship closes its eyes'
    print('plaintext =  ', plaintext)
    print()

    print('Testing Mode 0 (Stream Cipher):')
    ciphertext1 = solution_A3.e_permutation(plaintext, (key, 0))
    print('ciphertext = ', ciphertext1)
    plaintext1 = solution_A3.d_permutation(ciphertext1, (key, 0))
    print('plaintext2 = ', plaintext1)
    print()

    print('Testing Mode 1 (Block Cipher):')
    ciphertext2 = solution_A3.e_permutation(plaintext, (key, 1))
    print('ciphertext = ', ciphertext2)
    plaintext2 = solution_A3.d_permutation(ciphertext2, (key, 1))
    print('plaintext2 = ', plaintext2)
    print()

    print('Testing Mode 2 (Invalid Mode):')
    ciphertext3 = solution_A3.e_permutation(plaintext, (key, 2))
    print('ciphertext = ', ciphertext3)
    print()

    print('Testing Invalid key')
    key = 'abc'
    ciphertext3 = solution_A3.e_permutation(plaintext, (key, 2))
    print('ciphertext = ', ciphertext3)
    print("-------------------------------------------")
    print()
    return


# ----------------------------------------------------
# Test Q3: ADFGVX Cipher
# ---------------------------------------------------
def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: ADFGVX Cipher")
    print()

    plaintext = 'This is the final warning. End the war now!'
    key = 'Berlin'
    print('key       = ', key)
    print('plaintext = ', plaintext)
    ciphertext = solution_A3.e_adfgvx(plaintext, key)
    print('ciphertext =', ciphertext)
    plaintext2 = solution_A3.d_adfgvx(ciphertext, key)
    print('plaintext2 =', plaintext2)
    print("-------------------------------------------")
    print()
    return


# ----------------------------------------------------
# Test Q4: One Time Pad
# ---------------------------------------------------
def test_q4():
    print("-------------------------------------------")
    print("Testing Q4: One Time Pad")
    print()

    print('Testing xor_otp function:')
    char1 = ['A', 'r', '!', 'f']
    char2 = ['b', '?', 'p', 'Z']
    for i in range(len(char1)):
        print("xor({},{})= {}".format(char1[i], char2[i], solution_A3.xor_otp(char1[i], char2[i])))
    print()
    print('Testing encryption/decryption:')
    plaintext = 'Cryptography is amazing!'
    key = 'This Is Not a Random Key'
    print('key       = ', key)
    print('plaintext = ', plaintext)
    ciphertext = solution_A3.e_otp(plaintext, key)
    print('ciphertext= ', ciphertext)
    plaintext2 = solution_A3.d_otp(ciphertext, key)
    print('plaintext2= ', plaintext2)
    print("-------------------------------------------")
    print()
    return


# ----------------------------------------------------
# Test Q5: Myszkowski Cipher
# ---------------------------------------------------
def test_q5():
    print("-------------------------------------------")
    print("Testing Q1: Myszkowski Cipher")
    print()

    print('Testing get_keyOrder_myszkowski:')
    keys = [34, ['O', 'N', '0'], '', '034', '?=!', 'r', 'cc', 'Dad', 'Face', 'apple', 'good day', 'B!AA?CCCD']
    for key in keys:
        print('Key order for {} ='.format(key), end=' ')
        keyOrder = solution_A3.get_keyOrder_myszkowski(key)
        print(keyOrder)
    print()
    print('Testing encryption/decryption:')
    plaintext = 'AMIDSUMMERNIGHTSDREAM'
    key = 'Swindon'
    print('key       = ', key)
    print('key order = ', solution_A3.get_keyOrder_myszkowski(key))
    print('plaintext = ', plaintext)
    ciphertext = solution_A3.e_myszkowski(plaintext, key)
    print('ciphertext= ', ciphertext)
    plaintext2 = solution_A3.d_myszkowski(ciphertext, key)
    print('plaintext2= ', plaintext2)
    print()

    plaintext = 'The Taming of the Shrew'
    key = '"Deemed"'
    print('key       = ', key)
    print('key order = ', solution_A3.get_keyOrder_myszkowski(key))
    print('plaintext = ', plaintext)
    ciphertext = solution_A3.e_myszkowski(plaintext, key)
    print('ciphertext= ', ciphertext)
    plaintext2 = solution_A3.d_myszkowski(ciphertext, key)
    print('plaintext2= ', plaintext2)
    print()
    print("-------------------------------------------")
    return


test_q5()