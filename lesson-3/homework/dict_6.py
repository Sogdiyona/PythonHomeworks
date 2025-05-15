raw1 = input("Enter key-value pairs separated by commas (key:value): ")
raw2 = input("Enter key-value pairs separated by commas (key:value): ")
dict1 = {}
dict2 = {}

for pair in raw1.split(','):
    key, value = pair.strip().split(':')
    dict1[key.strip()] = value.strip()

for pair in raw2.split(','):
    key, value = pair.strip().split(':')
    dict2[key.strip()] = value.strip()
print({**dict1,**dict2})