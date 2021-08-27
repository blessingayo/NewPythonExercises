import json

file = open("seven.json.py", "r+")

file_data = json.load(file)

file_data.update({"cohort": "seven"})

file.seek(0)
json.dump(file_data, file)

print(file)