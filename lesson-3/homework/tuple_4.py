t = tuple(input("Enter tuple elements separated by spaces: ").split())
el=input("enter the element: ")
if el in t :
    print(f"{t} contains '{el}'")
else:
    print(f"{t} doesn't contain '{el}'")