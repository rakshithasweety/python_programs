a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))
if a>=b and b>=c:
    print("Highest number is",a)
elif b>=a and b>=c:
    print("Highest number is",b)
else:
    print("Highest number is",c)
    
