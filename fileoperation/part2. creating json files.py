import json  

# Defining a Python dictionary
data = {
    "name": "Aneeqah",
    "mail_id": "aneeqah@gmail.com",
    "phone_number": 67856785,
    "subject": ["data science", "big data", "data analytics"]
}

# Writing the dictionary to a JSON file
with open("data.json", "w") as f:
    json.dump(data, f)  # Convert and write dictionary to JSON format

# Reading the JSON file and loading it as a Python dictionary
with open("data.json", "r") as f:
    data1 = json.load(f)  # Deserialize JSON back into a dictionary

print(data1)  # Prints the entire dictionary
print(data1["subject"][1])  # Prints the second item in the 'subject' list: "big data"
