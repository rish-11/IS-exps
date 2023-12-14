def vernam_encrypt(plaintext, key) :
  return ''.join(chr(ord(p)^ord(k)) for p, k in zip(plaintext, key))

def vernam_decrypt(ciphertext, key) :
  return ''.join(chr(ord(c)^ord(k)) for c, k in zip(ciphertext, key))

print("Keep the Length of Plaintext and Key equal.")
plaintext = input("Enter the PlainText : ")
key = input("Enter the Key : ")

encrypted_text = vernam_encrypt(plaintext, key)
print("Encrypted Text : ", encrypted_text)
decrypted_text = vernam_decrypt(encrypted_text, key)
print("Decrypted Text : ", decrypted_text)
