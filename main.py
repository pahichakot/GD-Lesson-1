student = {
    'name': 'Pahi',
    'age': 11,
    'hobby': "Dance",
}

print(student)
print(student.keys())
print(student.values())

#Accessing values with keys
print(student["age"])
print(student["hobby"])

for i in student.keys():
    print(i," : ",student[i])

if "marks" in student:
    print("Key exists")
else:
    print("Key does not exist")

student["favorite food"] = "dosa"
print(student)

del(student["hobby"])
print(student)

food = input("What is your favorite food : ")
student["favorite food"] = food
print(student)

student["marks"] = [98, 76, 90, 94, 100]
print(student["marks"])

print(student["marks"][4])

#Nested dictionary
classroom = {
    "Pahi":{
        "age" : 11,
        "hobby" : "Dance"
    },

    "Ankitha":{
        "age" : 12,
        "hobby" : "Basketball"
    }
}
print(classroom.keys())
print(classroom.values())