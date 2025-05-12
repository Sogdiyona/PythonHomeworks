string=input("Enter the string: ")

if any(char.isdigit() for char in string):
    print("there is a digit")
else:
    print("there isn't a digit")