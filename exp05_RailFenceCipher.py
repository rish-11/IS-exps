def railfence_cipher(message, rails):
  fence = [''] * rails
  direction = 1
  row = 0

  for char in message:
    fence[row] += char
    row += direction
    if row==0 or row==rails-1:
      direction*=-1
  return ''.join(fence)

message = input("Enter a PlainText : ")
rails = int(input("Enter the Rails value : "))
encrypted_message = railfence_cipher(message, rails)
print("Encrypted Message : ", encrypted_message)