#dictionary is a collection of key value pairs that is unordered and mutuable

std = {"name":"sanjay" , "marks":99 , "subject":"fitness"}

print(std.keys())
print(std.values())
print(std.items())


#access elements in dic
{"name":"sanjay" , "marks":99 , "subject":"fitness"}

print(std["name"])
print(std["marks"])
print(std["subject"])

#change values in a dictionary
std["marks"] = 11

print(std["marks"])

#add new data to a dictionary
std["city"] = "vijayawada"

print(std) 

#remove data
std.pop("marks")

print(std)

print(std.get("name"))
#get() returns the value of the specified key

std.update({"age": 17})
#update() updates the value of the specified key

print(std)

std.pop("age")
#pop() removes the specified key and its value

print(std)

#popitem() removes the last inserted key-value pair
student ={"name" : "sanjay","age":17,"course" : "python"}

student.popitem()
print(student)

#set default

student = {"name" : "sanjay"}

student.setdefault("age",17)
print(student)

#clear method

student.clear()
print(student)

#copy method

student = {"name":"sanjay","age":17}

new_student = student.copy()

print(new_student)