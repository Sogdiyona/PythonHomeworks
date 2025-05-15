lst = input("Enter list elements separated by spaces: ").split()
element = input("Enter the element to insert: ")
index = int(input("Enter the index to insert at: "))
if 0 <= index <= len(lst):
    lst.insert(index, element)
    print("Updated list:", lst)
else:
    print("Invalid index!")