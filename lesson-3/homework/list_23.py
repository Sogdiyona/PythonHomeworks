numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers] 
filtered_numbers = [num for num in numbers if num % 2 != 0]
print(filtered_numbers)