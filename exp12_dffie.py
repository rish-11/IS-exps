def user_key():
    x1 = int(input("Enter user key(x1) : "))
    x2 = int(input("Enter user key(x2) : "))
    a = pow(3, x1) % p
    b = pow(3, x2) % p
    print("User Keys:")
    print("User A's key:", a)
    print("User B's key:", b)
    return a, b, x1, x2

def secret_key(a, b, x1, x2):
    k1 = pow(b, x1) % p
    k2 = pow(a, x2) % p
    print("Secret Keys:")
    print("User A's secret key:", k1)
    print("User B's secret key:", k2)
    if k1 == k2:
        print("Success! Shared secret keys match.")
    else:
        print("Try Again. Shared secret keys do not match.")

p = int(input("Enter a prime number (p) : "))
# q is not used, so it's removed

# User key generation
a, b, x1, x2 = user_key()

# Secret key computation
secret_key(a,b, x1, x2)
