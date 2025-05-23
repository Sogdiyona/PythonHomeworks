number=int(input("Enter the number: "))
for num in range(0,number+1):
    num+=1
    if number%num!=0:
        continue
    else:
        print(f"{num} is a factor of {number}")