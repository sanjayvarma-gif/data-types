#sets in python
#set is a collection of unique values that is unordered and mutable
numbers = {10,20,30,20,30}

print(numbers)


#why use sets
subjects = {"python", "java", "c++", "python"}
print(subjects)

#add values from a set
subjects = {"python","java"}
subjects.add("SQL")
print(subjects)

#remove value from a set
subjects = {"python", "java", "c++"}
subjects.remove("java")
print(subjects)

#dont allow duplicate values in a set
numbers = {10, 20, 30, 20, 30}
print(numbers)