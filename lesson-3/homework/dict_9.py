raw_input = input("Enter key-value pairs separated by commas (key:value): ")

pairs = raw_input.split(',')
items = {}
for pair in pairs:
    if ":" in pair:
        key, value = pair.strip().split(':')
        items[key.strip()] = value.strip()
if items:
    print("not empty")
else:
    print("empty") 