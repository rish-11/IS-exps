def encrypt(text, s):
  result = ''

  for i in range(len(text)):
    char = text[i]

    if char.isupper():
      result += chr((ord(char) + s - 65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)

  return result

text = input("Enter the PlainText : ")
s = int(input("Enter the shift value : "))
ciphertext = encrypt(text, s)
print("CipherText : ",ciphertext)


def decrypt(text, s):
  result = ''
  for i in range(len(text)):
    char = text[i]

    if char.isupper():
      result += chr((ord(char) + s - 65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)

  return result

ciphertext = input("CipherText : ")
s = int(input("Enter the shift value : "))
decrypted = decrypt(ciphertext,s)
print("Decrypted Text : ", decrypted)

#Brute force attack on Caesar Cipher

def brute_force_atttack(ciphertext):
  [print(f"Shift {s} : {decrypt(ciphertext,s)}") for s in range(26)]
brute_force_atttack(ciphertext)