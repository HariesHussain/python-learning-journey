#Program to check whether the roots of a quadratic equation are real and distinct, real and equal or imaginary
a = int(input("Ennter the integer a:"))
b = int(input("Enter the integer b:"))
c = int(input("Enter the integer c:"))
d = b*b - 4*a*c
if d > 0:
    print("Real and Distinct")
elif d == 0:
    print("Real and Equal")
else:
    print("Imaginary")