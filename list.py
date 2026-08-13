fruits = ["apple", "banana", "mango"]
print(fruits)

#list is mutable
fruits[1] = "orange"
print(fruits)

#accesing the item
print(fruits[0])

#negavtive indexin is also allowed
print(fruits[-1])

#append-add the item at the end
fruits.append("pineapple")
print(fruits)

#insert - add the item in the specific location
fruits.insert(1,"strawberry")
print(fruits)

#extend - adding multiple items
fruits.extend(["gauva", "papaya"])
print(fruits)

fruits.append(["rusk", "dates"])
print(fruits)

#`append()` → adds one item: `['apple', 'banana', ['mango', 'orange']]`; `extend()` → adds items separately: `['apple', 'banana', 'mango', 'orange']`.

#Removes an item by value.
fruits.remove("apple")
print(fruits)

#pop - removes the item by its index
fruits.pop(1)
print(fruits)

#pop - if the index is not provided, it removes the last item
fruits.pop
print(fruits)

#del - del can delete the entire list or js spefific item
del fruits[1]
print(fruits)

#clear - Removes all items, but the list itself remains.

#finding the the length of the list
print(len(fruits))

#Checking if an Item Exists
print("apple" in fruits)

print("apple" not in fruits)

# for fruit in fruits:
#     print(fruits)
    
    
#Slicing means taking a portion of a list.
print(fruits[1:3])
#Important rule

#The start index is included.

#The end index is not included.

#Slicing Shortcuts
print(fruits[1:])

#getting all the elements
print(fruits[:])

#slice with steps
print(fruits[0:3:2])
#list[start:end:step]

#reversing the string
fruits.reverse()

#sort() → arranges the list elements in ascending order by default.
numbers = [50, 10, 30, 20, 40]

numbers.sort()

print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(min(numbers))

#copying list