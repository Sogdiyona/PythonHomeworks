raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs = raw_input.split(',')
word={}
for pair in pairs:
    key, value = pair.strip().split(':')
    word[key.strip()] = value.strip()
print(word.keys())