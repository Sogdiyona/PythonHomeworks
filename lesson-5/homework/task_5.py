def is_prime(a):
    for num in range(2,int(a**0.5)+1):
        if a%num==0: 
          return False

    return True
a=int(input("Enter the number: "))
print(is_prime(a))
    
