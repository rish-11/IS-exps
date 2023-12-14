def encrypt(message, key):
    num_rows = len(key)

    while len(message) % num_rows != 0:
        message += ' '

    matrix = [message[i:i+num_rows] for i in range(0, len(message), num_rows)]

    ciphertext = ''
    for col in key:
        for row in matrix:
            ciphertext += row[col - 1]

    return ciphertext

message = input("Enter the message to encrypt: ").upper()
key = list(map(int, input("Enter the key as a permutation of numbers (e.g., 2 1 4 3): ").split()))

if sorted(key) != list(range(1, len(key) + 1)):
   print("Invalid key. The key must be a permutation of the numbers 1 to", len(key))
else:
    ciphertext = encrypt(message, key)
    print("\nEncrypted Message:", ciphertext)