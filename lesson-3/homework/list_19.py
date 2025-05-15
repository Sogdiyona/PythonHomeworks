lst = input("Enter list elements separated by spaces: ").split()
old_elem = input("Enter the element to replace: ")
new_elem = input("Enter the new element: ")
if old_elem in lst:
    index = lst.index(old_elem) 
    lst[index] = new_elem        
    print("Updated list:", lst)
else:
    print(f"Element '{old_elem}' not found in the list.")