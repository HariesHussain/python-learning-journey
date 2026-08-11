a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")