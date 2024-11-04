## Excercise 1
Fruits = ["Oranges", "Dragonfruits", "Mangoes", "Pineapples", "Apples"]
print(Fruits)

## Excercise 2
Colors = ["Red", "Black", "Dark Blue", "Beige", "Peach Pink"]
print("First element:", Colors[0])
print("Third element:", Colors[2])
print("Last element:", Colors[-1])

## Excercise 3
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

## Excercise 4
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

## Excercise 5
numbers = list(range(1, 11))
for number in numbers:
    print(number ** 2)

## Excercise 6
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

## Excercise 7
numbers = [45, 22, 88, 56, 92, 33]
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

## Excercise 8
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_a = letters.count('a')
print("The letter 'a' appears", count_a, "times.")

## Excercise 9
squares_of_evens = [x ** 2 for x in range(11) if x % 2 == 0]
print(squares_of_evens)

## Excercise 10
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)
