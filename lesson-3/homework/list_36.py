lst = input("Enter list elements separated by spaces: ").split()
lst=[float(num) for num in lst] 
positive_sum = sum(x for x in lst if x > 0)
print(positive_sum)