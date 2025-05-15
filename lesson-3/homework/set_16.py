set_1=set(input("Enter 1st set elements separated by spaces: ").split())
set_1 = [float(num) for num in set_1] 
filtered_numbers = [num for num in set_1 if num % 2 == 0]
print(filtered_numbers)