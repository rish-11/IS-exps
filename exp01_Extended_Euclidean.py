# Extended euclidean

def gcdExtended(a,b):
  if a==0:
    return b,0,1
  gcd,x1,y1 = gcdExtended(b%a, a)
  x = y1 - (b//a) * x1
  y = x1
  return gcd,x,y

a = int(input("Enter the first element a : "))
b = int(input("Enter the second element b : "))
gcdval, x, y = gcdExtended(a,b)
print(f"GCD({a}, {b}) = {gcdval}")
print(f"Coefficients(x,y) : ({x},{x})")