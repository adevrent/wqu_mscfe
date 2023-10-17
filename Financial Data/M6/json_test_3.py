# Python program to convert JSON to Python
import json

# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)

# Pretty Printing JSON string back
print(json.dumps(employee_dict, indent = 4, sort_keys= True))