numbers = input("Enter numbers separated by spaces: ").split() 
numbers = [int(num) for num in numbers]
odd=sum( 1 for num in numbers if num % 2 !=0 )
print(odd)