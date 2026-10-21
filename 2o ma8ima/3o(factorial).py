def factorial(n):
    if n==0:
        return 1
    else: 
        return n*factorial(n-1)
x = 15
y = 13
z = 11
print(x,"!=", factorial(x))
print(y,"!=", factorial(y))
print(z,"!=", factorial(z))