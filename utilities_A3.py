# --------------------------
# CP460 Fall 2019
# Assignment 3
# Utilities
# DO NOT CHANGE THIS FILE
# --------------------------

import string
import math


# Included Functions
#   1- file_to_text(fileName)
#   2- text_to_file(fileName)
#   3- get_lower()
#   4- shift_string(s,n,d)
#   5- load_dictionary(dictFile)
#   6- text_to_words(text)
#   7- analyze_text(text, dictFile)
#   8- is_plaintext(text, dictFile, threshold)
#   9- new_matrix(r,c,pad)
#   10- text_to_blocks(text,size)
#   11- get_adfgvx_square()
#   12- index_matrix(element,matrix)

# -----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
# -----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName, 'r')
    contents = inFile.read()
    inFile.close()
    return contents


# -----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
# -----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename, 'w')
    outFile.write(text)
    outFile.close()
    return


# -----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
# -----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a') + i) for i in range(26)])


# -------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
# -------------------------------------------------------------------
def shift_string(s, n, d):
    if d != 'r' and d != 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n * -1
        d = 'l' if d == 'r' else 'r'
    n = n % len(s)
    if s == '' or n == 0:
        return s

    s = s[n:] + s[:n] if d == 'l' else s[-1 * n:] + s[:-1 * n]
    return s


# -----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
# -----------------------------------------------------------
def load_dictionary(dictFile):
    inFile = open(dictFile, 'r', encoding=" ISO-8859-15")
    dictList = inFile.readlines()
    i = 0
    for word in dictList:
        dictList[i] = word.strip('\n')
        i += 1
    inFile.close()
    return dictList


# -------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list. 
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end 
# -------------------------------------------------------------------
def text_to_words(text):
    wordList = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i] != '':
                line[i] = line[i].strip(string.punctuation)
                wordList += [line[i]]
    return wordList


# -----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
# -----------------------------------------------------------
def analyze_text(text, dictFile):
    dictList = load_dictionary(dictFile)
    wordList = text_to_words(text)
    matches = 0
    mismatches = 0
    for word in wordList:
        if word.lower() in dictList:
            matches += 1
        else:
            mismatches += 1
    return (matches, mismatches)


# -----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
# -----------------------------------------------------------
def is_plaintext(text, dictFile, threshold):
    if text == '':
        return False
    result = analyze_text(text, dictFile)
    percentage = result[0] / (result[0] + result[1])
    if threshold < 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False


# -----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (str,int,double)
# Return:       empty matrix (2D List)
# Description:  Create an empty matrix of size r x c
#               All elements initialized to pad
#               Default row and column size is 2
# -----------------------------------------------------------
def new_matrix(r, c, pad):
    r = r if r >= 2 else 2
    c = c if c >= 2 else 2
    return [[pad] * c for i in range(r)]


# -----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
# ------------------------------------------------------------------------------
def text_to_blocks(text, size):
    return [text[i * size:(i + 1) * size] for i in range(math.ceil(len(text) / size))]


# ----------------------------------------------------
# Parameters:   None
# Return:       ADFGVX Square (2D list)
# Description:  Returns a 2D List
#               representing the polybius square to be used
#               in ADFGVX cipher
# ---------------------------------------------------
def get_adfgvx_square():
    return [['F', 'L', '1', 'A', 'O', '2'],
            ['J', 'D', 'W', '3', 'G', 'U'],
            ['C', 'I', 'Y', 'B', '4', 'P'],
            ['R', '5', 'Q', '8', 'V', 'E'],
            ['6', 'K', '7', 'Z', 'M', 'X'],
            ['S', 'N', 'H', '0', 'T', '9']]


# -----------------------------------------------------------
# Parameters:   element (str)
#               matrix (2D List)
# Return:       [r,c]
# Description:  returns position of a string element in a 2D
#               List, r = row number, c = column number
#               if not found --> return [-1,-1]
# -----------------------------------------------------------
def index_matrix(element, matrix):
    for r in range(len(matrix)):
        row = matrix[r]
        if element in row:
            return [r, row.index(element)]
    return [-1, -1]
