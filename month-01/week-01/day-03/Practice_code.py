import json

###### File Handling Practice

with open("my_notes.txt" , "w") as file:
    file.write("I am learning Python.\n")
    file.write("Today I learned file handling.\n")
    file.write("My goal is AI engineering.")


with open("my_notes.txt" , "r") as file:
    reading = file.read()

print(reading)

with open("my_notes.txt" , "a") as file:
    file.write("\nTomorrow I will learn APIs.")

with open("my_notes.txt", "r") as file:
    line = file.readlines()
print("Total Line:",len(line))


# Create a dictionary and save it

student = {
    "Name": "Rahul",
    "Age": 22,
    "Skills": ["Python", "FastAPI", "SQL"]
}

with open("Student.json" , "w") as file:
    json.dump(student , file , indent=4)


#  Read JSON data

with open("Student.json", "r") as file:
   user =  json.load(file)
print(user)



#  Convert dictionary into JSON string

user = {
    "name": "Alex",
    "role": "AI Engineer"
}

jason_data = json.dumps(user)

print(jason_data)
print(type(jason_data))


# Convert JSON string into dictionary

data = '{"name": "Alex", "age": 25}'

dict_data = json.loads(data)

print(dict_data)
print(type(dict_data))


