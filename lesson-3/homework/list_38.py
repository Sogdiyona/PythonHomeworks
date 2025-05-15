lst = input("Enter list elements separated by spaces: ").split()
if lst==lst[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    