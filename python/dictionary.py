import json

# declare a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": {
        "Python": "advanced",
        "Java": "intermediate",
        "C++": "beginner"
    }
}

# convert dictionary to json string
json_string = json.dumps(my_dict, indent=4)

# print json string
print(json_string)

# extract data from json string
data = json.loads(json_string)

# extract values from dictionary
name = data["name"]
age = data["age"]
city = data["city"]
languages = data["languages"]

# print values from dictionary
print("Name:", name)
print("Age:", age)
print("City:", city)
print("The languages I know & skill level are:")
# read values using for loop
for key, value in languages.items():
    print(key, ":", value)

# The below code is used to read data from a json file

# Open the json file
with open('example.json') as f:
    data = json.load(f)

# Extract data from the dictionary
name = data['name']
age = data['age']
city = data['city']
languages = data['languages']

# Print the extracted data
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print("Languages:")
for language, level in languages.items():
    print(f"- {language}: {level}")