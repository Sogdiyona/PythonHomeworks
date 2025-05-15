set_1=set(input("Enter 1st set elements separated by spaces: ").split())
el=input("Enter the element: ")
if el in set_1:
    print(" The element exist in the set list")
else:
    set_1.add(el)
    print(set_1)