raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs=raw_input.split(",")
items={}
for pair in pairs:
    key,value=pair.strip().split(":")
    items[key.strip()]=value.strip()
a=len(items)
print(a)