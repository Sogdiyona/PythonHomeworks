set_1=set(input("Enter 1st set elements separated by spaces: ").split())
set_2=set(input("Enter 2nd set elements separated by spaces: ").split())
if set_1.issubset(set_2):
    print("The first set is a subset of the second set.")
else:
    print("The first set is NOT a subset of the second set.")