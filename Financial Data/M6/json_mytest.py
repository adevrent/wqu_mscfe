import json

var = {"Name":"John", "Age":"30", "Gender":"Male", "Occupation":"SWE"}

with open("myjsonfile.json", "w") as p:
    json.dump(var, p)

with open("myjsonfile.json", "r") as read_it:
    mydata = json.load(read_it)
    
print("Name =", mydata["Name"])
print("Occupation =", mydata["Occupation"])