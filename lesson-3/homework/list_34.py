lst = input("Enter list elements separated by spaces: ").split()
k = int(input("Enter number of positions to shift right: "))
k = k % len(lst) if lst else 0
rotated = lst[-k:] + lst[:-k]
print("Rotated list:", rotated)