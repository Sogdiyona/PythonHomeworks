outer_raw = input("Enter outer key and a nested dictionary (format: key1:keyA=valA,keyB=valB): ")
outer_key, inner_raw = outer_raw.split(":")
inner_pairs = inner_raw.split(",")
nested_dict = {}
for pair in inner_pairs:
    k, v = pair.split("=")
    nested_dict[k.strip()] = v.strip()
data = {outer_key.strip(): nested_dict}
inner_key = input("Enter inner key to retrieve: ")
if inner_key in data[outer_key]:
    print("Value:", data[outer_key][inner_key])
else:
    print("Inner key not found.")