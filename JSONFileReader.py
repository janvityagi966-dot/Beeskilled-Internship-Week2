import json

# Open the JSON file
with open("data.json", "r") as file:
    data = json.load(file) #to convert JSON data into Python Data

# Print the JSON data in readable format
print("JSON Data:")
print(json.dumps(data, indent=4))

# Print the type of data
print(type(data))
