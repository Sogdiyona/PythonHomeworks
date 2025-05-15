word=input("Enter list elements separated by spaces: ").split()
start=input("enter the initial point of sublist: ")
end=input("enter the final point of sublist: ")
c=word.index(start)
d=word.index(end)
a=int(c)
b=int(d)
word = [int(x) for x in word]
sublist=word[a:b+1]
print(f"{max(sublist)}")