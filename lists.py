#insert numbers
#list is a mutuable
numbers = [10,20,30,40]
numbers.insert(1,15)
numbers.insert(2,25)

print(numbers)



     #extend numbers 
a= [1,2,3]
b = [4,5,6]

a.extend(b)
print(a)



#clear numbers
numbers = [10,20,30,40]
numbers.clear()
print(numbers)



#index method
numbers = [ 10,20,30,40,50,60,70,80,90]
print(numbers.index(20))
print(numbers.index(80))
print(numbers.index(50))


#count method
numbers = [10,16,25,35,45,16,25,45]
print(numbers.count(16))
print(numbers.count(25))
print(numbers.count(45))


#sort method 
numbers = [30,50,70,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)