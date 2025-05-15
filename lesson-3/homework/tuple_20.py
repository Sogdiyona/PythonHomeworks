word=tuple(input("Enter tuple elements separated by spaces: ").split())
n = int(input("Enter the number of elements per sublist: "))
sublists = [word[i:i+n] for i in range(0, len(word), n)]
print("Sublists:", sublists)