lst_1=tuple(input("Enter 1st tuple elements separated by spaces: ").split())
lst_2=tuple(input("Enter 2nd tuple elements separated by spaces: ").split())
print(f"{set(lst_1).union(set(lst_2))}")