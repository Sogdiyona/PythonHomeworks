import random
count = int(input("Enter how many unique random numbers you want: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if count > (end - start + 1):
    print("Range is too small to generate that many unique numbers.")
else:
    random_set = set( random.sample(range(start, end + 1), count))
    print("Random set:", random_set)