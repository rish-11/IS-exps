#Euclidean

def gcd(a,b):
  while a!=0:
    a, b = b%a, a
  return b
a = int(input("Enter the first element a : "))
b = int(input("Enter the second element b : "))
val=gcd(a,b)
print(f"GCD({a}, {b}) = {val}")