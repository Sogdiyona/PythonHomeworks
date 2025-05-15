lst = input("Enter list elements separated by spaces: ").split()
n = int(input("Enter the number of elements per sublist: "))
sublists = [lst[i:i+n] for i in range(0, len(lst), n)]
print("Sublists:", sublists)