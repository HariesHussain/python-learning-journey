a = int(input("Enter the angle a:"))
b = int(input("Enter the angle b:"))
c = int(input("Enter the angle c:"))

if a+b+c == 180:
    if a < 90 and b < 90 and c < 90:
        print("Acute Angle")
    elif a == 90 or b == 90 or c == 90:
        print("Right Angle")

    