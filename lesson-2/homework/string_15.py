string=input("Enter the string: ")
a=''.join(word[0].upper() for word in string.split())
print(a)
