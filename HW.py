#Homework
import random

name = input("What is your name : ")
age = int(input("What is your age : "))
hobby = input("What is a hobby you like to do : ")

student = {
    'name': name,
    'age': age,
    'hobby': hobby,
}    

for i in student.keys():
    print(i," : ",student[i])

access = input("What key would you like to access from your file (ex.name, age, hobby, etc.)")
if access == "name":
    print(student["name"])
elif access == "age":
    print(student["age"])
elif access == "hobby":
    print(student["hobby"])
else:
    print("Key does not exist")

food = input("What is your favorite food : ")
student["favorite food"] = food

remove = input("What key would you like to remove from your file : ")
del(student[remove])

for i in student.keys():
    print(i," : ",student[i])