# Creating a tuple
fruits = ('apple', 'banana', 'cherry')
print(fruits)
print(type(fruits))

#accessing elements
print(fruits[1])
print(fruits[-1])

#Unpacking tuples
colors = ('red', 'green', 'blue')
color1, color2, color3 =colors
print(color1)
print(color2)
print(color3)

#tuple concantenation
numbers1 = (1, 2 , 3)
numbers2 = (4, 5, 6)
numbers_combined = numbers1 + numbers2
print (numbers_combined)

#tuples slicing
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(alphabet[:3])
print(alphabet[-3:])
print(alphabet[::2])

#Tuples Methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4))
print(numbers.index(2))
