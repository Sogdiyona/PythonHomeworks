set_1=set(input("Enter 1st set elements separated by spaces: ").split())
set_2=set(input("Enter 2nd set elements separated by spaces: ").split())
a=set_1.union(set_2)
print(set(a))