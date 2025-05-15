word=input("Enter list elements separated by spaces: ").split()
index=int(input("Enter the index: "))
if 0<=index<len(word):
   a=word.pop(index)
   print(word)
else :
    print("invalid index")