t=tuple(input("Enter the list: ").split())
t=[float(num) for num in t]
a=sorted(t)
print(f"{a[-2]}")
