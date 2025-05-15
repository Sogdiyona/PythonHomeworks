raw_input = input("Enter key-value pairs separated by commas (key:value): ")
pairs=raw_input.split(",")
items={}
min_value = int(input("Введите минимальное значение для фильтрации: "))
for pair in pairs:
    key,value=pair.strip().split(":")
    items[key.strip()]=int(value.strip())
a={key: value for key, value in items.items() if value<= min_value }
print(a)