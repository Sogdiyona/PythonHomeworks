word=input("Enter list elements separated by spaces: ").split()
a=list(word)
if len(a)%2==0 :
    c=len(a)//2
    print(f"{a[c-1], a[c]}")
else:
    d=len(a)//2+1
    print(a[d])