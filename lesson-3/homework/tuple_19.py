word=tuple(input("Enter tuple elements separated by spaces: ").split())
el=input("element: ")
a=list(word)
if el in a:
    a.remove(el)
    word = tuple(a)
    print(word)
else:
     print("Element not found in the tuple.")

