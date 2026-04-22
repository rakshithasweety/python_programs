student={
    "name":"Ravi",
    "age":18,
    "course":"Engineering"
    }
key=input("Enter key to search:")
if key in student:
    print("key found!value:",student[key])
else:
     print("key not found")
