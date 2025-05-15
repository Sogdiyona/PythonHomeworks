word=tuple(input("Enter tuple elements separated by spaces: ").split())
el=input("element: ")
indices = [i for i, x in enumerate(word) if x == el]
print(indices)