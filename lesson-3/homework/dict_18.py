from collections import defaultdict
data = defaultdict(lambda: "Not Found")
pairs = input("Enter key-value pairs separated by commas (key:value): ").split(',')
for pair in pairs:
    if ':' in pair:
        key, value = pair.strip().split(':')
        data[key.strip()] = value.strip()
key_to_find = input("Enter a key to retrieve its value: ")
print("Value:", data[key_to_find])