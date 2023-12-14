def construct_playfair_matrix(key):
  key = key.replace(" ","").upper()
  matrix = [['' for _ in range(5)] for _ in range(5)]
  alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

  key_set = set()
  row,col = 0,0

  for char in key:
    if char not in key_set:
      matrix[row][col] = char
      key_set.add(char)
      col += 1
      if col==5:
        col=0
        row+=1

  for char in alpha:
    if char not in key_set:
      matrix[row][col] = char
      col += 1
      if col==5:
        col=0
        row+=1

  return matrix


def print_playfair_matrix(matrix):
  for row in matrix:
    print(''.join(row))

def preprocess_text(text):
  text = text.replace(" ","").upper()
  text_pairs = [text[i:i+2] for i in range(0,len(text),2)]

  for i in range(len(text_pairs)):
    if len(text_pairs[i]) == 1:
      text_pairs[i] += "X"

  return text_pairs

def encrypt(plaintext,key):
  matrix = construct_playfair_matrix(key)
  plaintext = preprocess_text(plaintext)
  ciphertext = []

  for pair in plaintext:
    a, b = pair[0], pair[1]
    a_row,a_col,b_row,b_col = 0,0,0,0

    for i in range(5):
      for j in range(5):
        if matrix[i][j]==a:
          a_row, a_col = i,j
        if matrix[i][j]==b:
          b_row,b_col = i,j

    if a_row == b_row:
      ciphertext.append(matrix[a_row][(a_col+1)%5] + matrix[b_row][(b_col+1)%5])
    elif a_col == b_col:
      ciphertext.append(matrix[(a_row+1)%5][a_col] + matrix[(b_row+1)%5][b_row])
    else:
      ciphertext.append(matrix[a_row][b_col] + matrix[a_col][b_row])

  return ''.join(ciphertext)


key = input("Enter the Key : ")
matrix = construct_playfair_matrix(key)
print("\nPlayfair Matrix : ")
print_playfair_matrix(matrix)

plaintext = input("\nEnter the PlainText : ")
encrypted_text = encrypt(plaintext, key)
print("\nPlain Text : ", plaintext)
print("Cipher Text : ", encrypted_text)