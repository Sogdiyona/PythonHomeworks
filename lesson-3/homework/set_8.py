set_1=set(input("Enter 1st set elements separated by spaces: ").split())
el=input("enter the element: ")
if el in set_1:
    set_1.remove(el)
    print(set_1)
else:
    print("the given element isn't in set")