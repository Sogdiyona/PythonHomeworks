raw_input = input("Enter key-value pairs separated by commas (key:value): ")
key1 = input("Enter the key to check: ")
pairs = raw_input.split(',')
items = {}
for pair in pairs:
    key, value = pair.strip().split(':')
    items[key.strip()] = value.strip()
if key1 in items: 
    print(items.get(key1))
else:
    print("key doesn't exist")