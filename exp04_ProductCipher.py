def railfence_cipher(message, rails):
  fence = ['']*rails
  direction = 1
  row = 0

  for char in message:
    fence[row] += char
    row += direction
    if row==0 or row==rails-1:
      direction*=-1
  return ''.join(fence)

def caesar_cipher(text,s):
  result = ''
  for char in text:
    if char.isalpha():
      if char.isupper():
        result += chr((ord(char) + s - 65) % 26 + 65)
      else:
        result+=chr((ord(char) + s - 97) % 26 + 97)
    else:
      result+=char
  return result

def product_cipher(message,rails,s):
  railfence_encrypted = railfence_cipher(message, rails)
  productcipher_encrypted = caesar_cipher(railfence_encrypted, s)
  return productcipher_encrypted

message = "HELLO"
rails = 3
s = 3

encrypted_message = product_cipher(message,rails,s)
print("Original Message : ", message)
print("Encrypted Message : ", encrypted_message)