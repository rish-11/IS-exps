import math

def encrypt(key, message):
    numColumns = len(key)    #determines no. of cols based on len of keys
    numRows = int(math.ceil(len(message) / numColumns))  #calculates the number of rows needed to accommodate the message
    numBlanks = (numColumns * numRows) - len(message)

    plaintext = message + (' ' * numBlanks)
    cipherText = [''] * numColumns   #initializes a list to store the encrypted text, with each element representing a column.

    col = 0
    for char in plaintext:
        cipherText[col] += char
        col += 1
        if col == numColumns:
            col = 0

    return ''.join(cipherText)

message = input("Enter message: ")
key = input("Enter the Key: ")
text = encrypt(key, message)
print(text)

