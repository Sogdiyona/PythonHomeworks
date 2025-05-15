raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs=raw_input.split(",")
items={}
value1=input("enter the value: ")
for pair in pairs:
    key,value=pair.strip().split(":")
    items[key.strip()]=value.strip()
swapped={v: k for k, v in items.items() }
if value1 in swapped:
    print(swapped[value1])
else:
    print("value doesn't exist")