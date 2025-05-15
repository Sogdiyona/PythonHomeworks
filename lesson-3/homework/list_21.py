numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers] 
a=sorted(numbers)
print(f"{a[1]}")