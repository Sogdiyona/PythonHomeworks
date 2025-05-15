lst = input("Enter list elements separated by spaces: ").split()
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)

print(unique)