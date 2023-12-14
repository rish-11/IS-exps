import random
p = int(input('Enter a prime number: '))
g = int(input('Enter a number: '))

def generate_random_number():
    return random.randint(1, p)

def publish_private_number(arr):
    return [(g**a) % p for a in arr]

def compute_secret_key(public_key, private_number):
    return (public_key**private_number) % p

# Alice
alice_n = generate_random_number()
alice_ga = publish_private_number([alice_n])

# Bob
bob_n = generate_random_number()
bob_gb = publish_private_number([bob_n])

# Eve
eve_a = generate_random_number()
eve_b = generate_random_number()
eve_gea_gb = publish_private_number([eve_a, eve_b])

# Printing selected private numbers
print(f'Alice selected (a): {alice_n}')
print(f'Bob selected (b): {bob_n}')
print(f'Eve selected private number for Alice (c): {eve_a}')
print(f'Eve selected private number for Bob (d): {eve_b}')

# Publishing values
print(f'Alice published (ga): {alice_ga[0]}')
print(f'Bob published (gb): {bob_gb[0]}')
print(f'Eve published value for Alice (gc): {eve_gea_gb[0]}')
print(f'Eve published value for Bob (gd): {eve_gea_gb[1]}')

# Computing secret keys
alice_secret = compute_secret_key(eve_gea_gb[0], alice_n)
eve_secret_alice = compute_secret_key(alice_ga[0], eve_a)
bob_secret = compute_secret_key(eve_gea_gb[1], bob_n)
eve_secret_bob = compute_secret_key(bob_gb[0], eve_b)

# Printing computed secret keys
print(f'Alice computed (S1): {alice_secret}')
print(f'Eve computed key for Alice (S1): {eve_secret_alice}')
print(f'Bob computed (S2): {bob_secret}')
print(f'Eve computed key for Bob (S2): {eve_secret_bob}')