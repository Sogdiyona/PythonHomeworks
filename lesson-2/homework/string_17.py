s=input("enter the string: ")
si=input("enter the symbol: ")
vowels="aeiouy"
a= ''.join(si if char.lower() in vowels else char for char in s)
print(a)