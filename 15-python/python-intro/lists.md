## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lists in Python

### Learning Objectives
*After this lesson, you will be able to:*
- Create lists in Python.
- Print out specific elements in a list.
- Perform common list operations.

## Lists

### What is a list?

A list is Python's name for an array. They function very similarly to Javascript arrays.

```python
# Declaring lists
colors = ["red", "yellow", "green"]
my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo"]

# Strings
colors = ["red", "yellow", "green"]

# Numbers
my_nums = [4, 7, 9, 1, 4]

# Both!
loosy_goosy = ["red", 7, "yellow", 1, 4]
```
If you want to access a specific element, you access it with bracket notations in the same way as Javascript. For example, to print 'Steve', we would write: `print(my_class[2])`.

## List Operations

### Basic List Operations

#### `len()`

To get the length of a list, use `len(list_name)`.
For example:
```python
my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo"]

num_students = len(my_class)
print("There are", num_students, "students in the class")
# => 5
```

#### `append()`
To add something on the end of a list, use `list_name.append(item)`.
For example:
```python
my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo"]

my_class.append("Sonyl")
print(my_class)
# => ["James", "Zoe", "Steve", "Nhu", "Paulo", "Sonyl"]
```

#### `insert()`
To add an element in a list at a specific index, use `list_name.insert(index, item)`.
For example:
```python
my_class = ["James", "Zoe", "Steve", "Nhu", "Paulo", "Sonyl"]

my_class.insert(1, "Kelly")
print(my_class)
# => ["James", "Kelly", "Zoe", "Steve", "Nhu", "Paulo", "Sonyl"]
```

#### `pop()`
There are two ways to use `pop()`; with no parameters or with an index. **If no parameter is set, `pop()` will remove the last item from a list and return it**, otherwise it will remove the item at that specific index.
For example:
```python
my_class = ["James", "Kelly", "Zoe", "Steve", "Nhu", "Paulo", "Sonyl"]

student_that_left = my_class.pop()
print(student_that_left, "has left the class.")
# => "Sonyl has left the class"
print(my_class)
# => ["James", "Kelly", "Zoe", "Steve", "Nhu", "Paulo"]

second_student_to_leave = my_class.pop(1)
print(student_that_left, "has left the class.")
# => "Kelly has left the class"
print(my_class)
# => ["James", "Zoe", "Steve", "Nhu", "Paulo"]
```

### Test it out!

1. Declare a list with the names of your classmates
2. Print out the length of that list
3. Add a new classmate
4. Print the 3rd name on the list
5. Delete the first name on the list
6. Move the last name on the list to be the second name

<details><summary>Answers</summary>
<p>

```python
# 1. Declare a list with the names of your classmates
classmates = ["James", "Tamis", "Parker", "Nhu", "Brad", "Q", "Kelly", "Paulo", "Doug"]
# 2. Print out the length of that list
print(len(classmates))
# 3. Add a new classmate
classmates.append("Taylor")
print(classmates)
# 4. Print the 3rd name on the list
print(classmates[2])
# 5. Delete the first name on the list
print(classmates.pop(0))
# 6. Move the last name on the list to be the second name
classmates.insert(1, classmates.pop())
print(classmates)

```

</p>
</details>

### Numerical List Operations

These actions can only be used with lists of numbers.

#### `sum()`

This is used when you want to add all the numeric items in your list.
For example:
```python
# sum(numeric_list)

batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(batting_avgs)
print("The total of all the batting averages is", sum_avgs)
# => 2.409
```

#### `min()` and `max()`

These will find the smallest and largest number in your list.
For example:
```python
# max(numeric_list)
# min(numeric_list)

batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
print("The highest batting average is", max(batting_avgs))
# => 0.328
print("The lowest batting average is", min(batting_avgs))
# => 0.208
```

### Test it out!

1. Declare a list of numbers
2. Print out the largest difference between numbers
3. Print the mean of all the numbers

<details><summary>Answers</summary>
<p>

```python
# Declare a list of numbers
numberz = [4, 10, 8, 9, 77, 21, 3, 4]
# Print out the largest difference between numbers
big_diff = max(numberz) - min(numberz)
print(big_diff)
# Print the mean of all the numbers
avg = sum(numberz)/len(numberz)
print(avg)
```

</p>
</details>

## Additional Resources

- [Python Lists - Khan Academy Video](https://www.youtube.com/watch?v=zEyEC34MY1A)
- [Google For Education: Python Lists](https://developers.google.com/edu/python/lists)
- [Python-Lists](https://www.tutorialspoint.com/python/python_lists.htm)
