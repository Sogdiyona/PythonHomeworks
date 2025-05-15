t=tuple(input("Enter the list: ").split())
if t==t[::-1]:
    print("palindrome")
else:
    print("not palindrome")