import random

def gcd(a,b):
  if a!=0:
    a,b = b%a,a
  return b


def multiplicative_inverse(e,phi):
  d=0
  x1=0
  x2=1
  y1=1
  temp_phi = phi
  while e>0:
    temp1 = temp_phi//e
    temp2 = temp_phi - temp1 * e
    temp_phi = e
    e = temp2

    x = x2 - temp1 * x1
    y = d - temp1 * y1

    x1=x
    y1=y
    x2=x1
    d=y1


  if temp_phi==1:
    return d + phi
  

def isprime(num):
  if num==2:
    return True
  elif num<2 or num%2==0:
    return False
  for n in range(3, int(num**0.5)+2, 2):
    if num%n==0:
      return False
  return True

def generate_pairs(p,q):
  if not(isprime(p) and isprime(q)):
    print("p and q both should be prime numbers.")
  if p==q:
    print("p and q should not be equal.")

  n = p*q
  phi = (p-1)*(q-1)
  e = random.randrange(1,phi)
  g = gcd(e,phi)
  while g!=1:
    e = random.randrange(1,phi)
    g = gcd(e,phi)
  d = multiplicative_inverse(e,phi)

  return ((e,n), (d,n))

def encrypt(pk, plaintext):
  key,n = pk
  cipher = [pow(ord(char),key,n) for char in plaintext]
  return cipher 

p = int(input("enter a prime num : "))
q = int(input("enter anoher prime no : "))
print("generating pairs")
public, private = generate_pairs(p,q)
print(f"Your public key pair is {public}, your private key pair is {private}")
message = input("enter a message to encrypt : ")
encrypted_message = encrypt(public, message)
print("Your encrypted message is : ", ''.join(map(lambda x:str(x), encrypted_message)))



# RSA CODE + RSA DIGITAL SIGNATURE

def sign(sk, message):
    key, n = sk
    signature = pow(int.from_bytes(message.encode(), byteorder='big'), key, n)
    return signature

def verify(pk, message, signature):
    key, n = pk
    decrypted_signature = pow(signature, key, n)
    return int.from_bytes(message.encode(), byteorder='big') == decrypted_signature

message = input("Enter a message to sign and encrypt: ")

# Sign the message
signature = sign(private, message)

# Encrypt the message
encrypted_message = encrypt(public, message)

print("Your signed and encrypted message is:", ''.join(map(lambda x: str(x), encrypted_message)), signature)

# Verification
if verify(public, message, signature):
    print("Signature verification successful.")
else:
    print("Signature verification failed.")