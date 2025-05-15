t=tuple(input("Enter the list: ").split())
start=input("enter the initial point of subtuple: ")
end=input("enter the final point of subtuple: ")
c=t.index(start)
d=t.index(end)
a=int(c)
b=int(d)
t = [int(x) for x in t]
subtuple=t[a:b+1]
print(f"{min(subtuple)}")