raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs = raw_input.split(',')
word={}
key_to_check = input("Enter the key to check: ")
for pair in pairs:
    key, value = pair.strip().split(':')
    word[key.strip()] = value.strip()
if key_to_check in word:
    print(f"Key '{key_to_check}' is present in the dictionary.")
else:
    print(f"Key '{key_to_check}' is NOT present in the dictionary.")