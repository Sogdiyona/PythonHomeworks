my_set = set(input("Enter set elements separated by spaces: ").split())

if my_set:
    removed_element = my_set.pop()
    print("Removed element:", removed_element)
    print("Set after removal:", my_set)
else:
    print("Set is empty.")