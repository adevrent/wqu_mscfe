import json

var = { 
	"Subjects": {
				"Maths":85,
				"Physics":90
				}
	}

# print(type(var))  # it is dict type.

# Create a file named Sample.json and open it with write mode.
with open("Sample.json", "w") as p:
	json.dump(var, p)  # Here, the dump() takes two arguments: first, the data object to be serialized,
                        # and second the object to which it will be written(Byte format). 

# Open Sample.json with read mode
with open("Sample.json", "r") as read_it:
	data = json.load(read_it)  # .load() method converts the JSON string to dict object
print("Type of 'data' =", type(data))
print(data)