t=tuple(input("Enter the list: ").split())
unique = []
for item in t:
    if item not in unique:
        unique.append(item)

print(unique)