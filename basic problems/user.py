#Program to check whether the input character is an uppercase letter, lowercase letter, digit or special character
a = input("Enter a characcter a: ")
if a.isupper():
     print("Uppercase")
elif a.islower():
    print("Lowercase")
elif a.isdigit():
    print("Digit")
else:
    print("Special Character")