def f(n, a=0, b=1):
    
    if a > n:
        return
    print(a, end=" ")
    
    f(n, b, a + b)

num = int(input("Enter the maximum value: "))
f(num)