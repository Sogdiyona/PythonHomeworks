raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs = raw_input.split(',')
key1 = input("Enter the key to check: ")
word={}
for pair in pairs:
    key, value = pair.strip().split(':')
    word[key.strip()] = value.strip()
if key1 in word:
    removed=word.pop(key1)
    print(f"key {key1} was removed")
else:
    print(f"{key1} doesn't exist")
print(word)