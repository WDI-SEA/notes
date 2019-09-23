# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Sets and Tuples in Python

### Learning Objectives
*After this lesson, you will be able to:*
- Perform common actions with sets.
- Perform common actions with tuples.
- Know when to use different data structures.

## Sets

We know that we can keep data in a list format.
```python
unique_colors = ["red", "yellow", "red", "green", "red", "yellow"]
subscribed_emails = ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
```
What might be the problem with these two examples?

In the first list, we have repetition in `unique_colors` section, making them not unique! The second example is more of a use case. If you wanted to keep track of subscribers by email, `len(subscribed_emails)` wouldn't give you an accurate number because of the duplicates.

### Enter the Set

```python
unique_colors_set = {"green", "yellow", "red"}
subscribed_emails_set = {"mary@gmail.com", "opal@gmail.com", "sayed@gmail.com"}
```
Notice the `{}` versus the `[]`.

A *list* is a collection of *elements*, contained within square brackets `[]`.

However, there is a specific version of a *list* called a *set*. What makes a set different is that all of the *elements* in a *set* must be unique. That is to say, nothing can appear more than once in a *set*. Sets are defined with curly braces `{}`.

A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python’s set class represents the mathematical notion of a set. 

### Making a Set

We can make a set directly as above, declaring it and placing the values in curly brackets rather than square brackets. 

The other way to create a set is by using `set()` with a pre-existing list. 

```python
# my_set = set(a_list_to_convert)

unique_colors_list = ["red", "yellow", "red", "green", "red", "yellow"]
unique_colors_set = set(unique_colors_list)
# => {"green", "yellow", "red"}
```

Instead of passing a list into `set()`, we could just type a list directly in:
```python
# my_set_2 = (["enter", "list", "here"])

unique_colors_set_2 = set(["red", "yellow", "red", "green", "red", "yellow"])
# => {"green", "yellow", "red"}
```

When making a set via a list Python removes duplicates automatically.

### Why Sets?

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set

### Important Note: Sets

Lists are always in the same order:

- `my_list = ["green", "yellow", "red"]` is always going to be`["green", "yellow", "red"]`
- `my_list[0]` is always  `"green"`; `my_list[1]` is always `"yellow"`; `my_list[2]` is always `"red"`.

Sets are not! Like dictionaries, they're in any order.

- `my_set = {"green", "yellow", "red"}` could later be `{"red", "yellow", "green"}`!
- `my_set[0]` could be `"green"`, `"red"`, or `"yellow"` - we don't know!

We **cannot** do:  `print(my_set[0])` - it could be anything! Python won't let us.

### Test it out

Let's pull up a new `set_practice.py` file and make some sets!

- Make a list `clothing_list` containing the main color of your classmates' clothing.
- Using `clothing_list`, make a set named `clothing_set`.
- Use a `for` loop to print out both `clothing_list` and `clothing_set`.
- Try to print an index!

<details>
    <summary>Answers</summary>
    ```python
    clothing_list = ["red", "black", "brown", "black", "purple"]

    clothing_set = set(clothing_list)

    for item in clothing_list:
      print(item)
    for item in clothing_set:
      print(item)
      
    for i in range(len(clothing_set)):
      print(clothing_set[i])
    # => TypeError: 'set' object does not support indexing
    ```

</details>

### Adding to a Set

How do we add more to a set?

```python
# In a list:
clothing_list.append("red")

# In a set
clothing_set.add("red")
```

Why is it `append()` in lists but `add()` in sets? It's because we can't guarantee it's going at the end!

Let's a few colors to `clothing_list` and `clothing_set`, then print them.

- What happens if you add a duplicate?

### Removing from a Set

Remember, lists are always the same order: `["green", "yellow", "red"]`.

- `my_list[0]` is always "green".

Remember, sets are not!

- With the set `{"green", "yellow", "red"}`, `my_set[0]` could be `green`, `red`, or `yellow`.

The same way, we need to be careful about removal:

```python
# In a list:
clothing_list.pop() # Removes and returns the last item in the list.
clothing_list.pop(0) # Removes and returns a specific (here, the first) item in the list.

# In a set
clothing_set.pop() # No! This is unreliable! The order is arbitrary.
clothing_set.pop(0) # No! Python throws an error! You can't index sets.
clothing_set.remove('red') # Do this! Call the element directly!
```

## Tuples

A set is a type of list which doesn't allow duplicates.

What if, instead, we have a list we don't want to change? What if we wanted that data to be immutable?

```python
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
```

We **don't** want:
```python
rainbow_colors[0] = ("gray")
## Gray's not in the rainbow!
rainbow_colors.pop()
## We can't lose violet!
rainbow_colors.append("pink")
# Pink's not in the rainbow!
```

We want `rainbow_colors` to be **immutable** - the list _cannot_ be changed.

How we do that in Python?

### Enter the Tuple

**Sets** are one specific type of list.

- No duplicates 
- Mutable.
- Uses `{}`

**Tuples** are another specific type of list.

- Duplicates
- Immutable.
- A list that _cannot_ be changed.
- Uses `()`

Going back to the rainbow list we defined earlier. We want to make that a tuple:
```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

### Why Tuples?

Tuples are useful when you need data protection through immutability—when you never want to change the list. You can still access them through indexes (because the data never changes, including the position!)

## Tuple Syntax

- Created with parentheses `()`.
- Access values via indices (like regular lists, but *not* like sets).

```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
print(rainbow_colors[1])
# Prints "orange"
```

Tuples can be printed with a `for` loop (just like a set or list!).

```python
rainbow_colors_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")

for color in rainbow_colors_tuple:
  print(color)
```

### Test it out
- Let's declare a tuple named `seasons` and set it to have the values `fall`, `winter`, `spring`, and `summer`. 
- We'll print the tuple and each value. 
- Then we'll try to reassign them.

<details><summary>Answers</summary>
<p>

```python
seasons = ("fall", "winter", "spring", "summer")

print(seasons)
for season in seasons:
    print(season)

seasons[0] = "autumn"
# => TypeError: 'tuple' object does not support item assignment
```
</p>
</details>

## Quick Review: Sets, Tuples, Lists

**List**:

- The original, normal object: `["red", "red", "yellow", "green"]`.
- Has duplicates; mutable: `append()`, `insert(index)`, `pop()`, `pop(index)`

**Set**:

- List without duplicates: `{"red", "yellow", "green"}`.
- Mutable: `add()` and `remove(element)`

**Tuple**:

- Has duplicates, but immutable: You can't change it!
- `("red", "red", "yellow", "green")` will *always* be `("red", "red", "yellow", "green")`.

## Types

Variables certainly can hold a lot of different types of data! We've just been learning that sets, tuples, and lists are similar, but easily confused. How do we tell?

`type()` tells us what a variable is: set, tuple, list, dictionary, integer, string - anything!

## Additional Reading

- [Repl.it that recaps Tuples](https://repl.it/@SuperTernary/python-programming-tuple-practice?lite=true)
- [Python Count Occurrences of Letters, Words and Numbers in Strings and Lists-Video](https://www.youtube.com/watch?v=szIFFw_Xl_M)
- [Storing Multiple Values in Lists](https://swcarpentry.github.io/python-novice-inflammation/03-lists/)
- [Sets and Frozen Sets](https://www.python-course.eu/sets_frozensets.php)
- [Sets](https://www.learnpython.org/en/Sets)
- [Python Tuple](https://www.programiz.com/python-programming/tuple)
- [Tuples](http://openbookproject.net/thinkcs/python/english3e/tuples.html)
- [Strings, Lists, Tuples, and Dictionaries Video](https://www.youtube.com/watch?v=19EfbO5D_8s)
- [Python Data Structures: Lists, Tuples, Sets, and Dictionaries Video](https://www.youtube.com/watch?v=R-HLU9Fl5ug)
