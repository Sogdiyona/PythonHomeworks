number=input("enter numbers(only numbers and spaces are allowed): ").split(" ")
if  all(char.isdigit() or char.isspace() for char in number) :
    number=[int(num) for num in number]
    print(f"{sum(number)}")
else :
    print("please enter only numbers and spaces")