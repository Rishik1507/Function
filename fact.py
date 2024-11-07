def factorial(n):
    if n==1:
        return n
    else:
       return n*factorial(n-1)
a= int(input("Enter the number: "))
if a<0:
    print("No factorial")
elif a==0:
    print("Factorial is 0")
else:
    print("Factorial is",factorial(a))
    