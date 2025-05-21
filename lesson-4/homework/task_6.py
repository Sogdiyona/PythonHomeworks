for num in range(1,100):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0 and num>1:
            prime=False
            continue
    if prime:
        print(num)
