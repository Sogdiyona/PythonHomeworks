raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs=raw_input.split(",")
items={}
for pair in pairs:
    key,value=pair.strip().split(":")
    items[key.strip()]=value.strip()
key1=input("key to update: ")
key2=input("key uptade with: ")
if key1 in items:
    items[key1]=key2
    print(items)
else:
    print("key doesn't exist")