#Program to check whether the input character is an alphabet, digit or special character
a = input("Enter a Character :")
if (a.isalpha()):
    print("Alphabet")
elif ('0' <= a <= '9'):
    print("Digit")
else:
    print("Special Character")