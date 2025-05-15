numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers] 

largest = min(numbers)
print(f"The largest number is: {largest}")
print("-"*60)
word=input("Enter words separated by spaces: ").split()
large=min(word, key=len)
print(large)