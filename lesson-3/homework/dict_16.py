import json
raw_input = input("Enter a JSON-style dictionary: ")

try:
    data = json.loads(raw_input)
    has_nested_dict = any(isinstance(value, dict) for value in data.values())
    print("Contains nested dictionary:", has_nested_dict)
except json.JSONDecodeError:
    print("Invalid input. Please enter valid JSON.")