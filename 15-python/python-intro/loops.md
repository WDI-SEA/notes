## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Loops in Python

### Learning Objectives
*After this lesson, you will be able to:*
- Use a `for` loop to iterate a list.
- Use `range()` to dynamically generate loops.
- Use a `while` loop to control program flow.


## For Loops

For loops in Python follow this structure:
```python
for item in collection:
  # Do something with item
```
Look familiar? This syntax is very similar to a for/in loop in javascript!

Here's an example of iterating through a list of colors:
```python
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for color in visible_colors:
  print(color)
```

The loop runs for every item in the list - the length of the collection. Here, it runs 6 times. 

We've seen that you can use a for loop to loop through a list, but python loops can do more than that.

### Loop through a string

```python
my_string = "Hello, world!"

for character in my_string:
  print(character)
# prints each character on a new line (including the whitespace!)
```

### Looping for a specific number of iterations

If you want to get specific on the number, you can use `range()`. It is a built in method that accepts an integer and returns a range object, which is nothing but a sequence of integers. 
In a for loop, it looks like this:
```python
for i in range(10):
    print(i)
# this will print out 1-9
```

`range()` takes three arguments, the first and last of which are optional.
```python
range([start,] stop [, step])
```
Because indexing starts at 0, the default start is 0 and the stop is not inclusive.

> If you want a list of range integers, you can do so by calling `range_list = list(range(10))`


#### `range(x)`

When called with one parameter, range will run 0-x, exclusive. This is particularly useful when you want to have an index number while looping through a list—like in situtations where you want to mutate the data in the array you are iterating through.
For example:
```python
# Add one to a list of numbers

numz = [3, 8, 10, 4, 0.4, 1.5]

for num in numz:
    num += 1
print(numz)
# => [3, 8, 10, 4, 0.4, 1.5]

for i in range(len(numz)):
    numz[i] += 1 
# => [4, 9, 11, 5, 1.4, 2.5]
```

#### `range(x, y)`

When called with two parameters, range will produce a range object starting at `x` and `y` (exclusive).
For example:
```python
# Print the last three colors of the rainbow
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for i in range(len(visible_colors)-3, len(visible_colors)):
    print(visible_colors[i])
```

#### `range(x, y, z)`

When called with three parameters, the last parameter functions as a step meaning the range will increment (or decrement) by that amount.
For example:
```python
# Print even numbers in a range
for i in range(0, 11, 2):
    print(i)

# Print a countdown
for i in range(10, 0, -1):
    print(i)
print("KABOOM")
```

### Try it for yourself

This one is a bit of a challenge. Make a list of strings (all lowercase). Iterate through your list and mutate it so that each string has the first letter capitalized.

<details><summary>Answer</summary>
<p>

```python
# Capitalize the first letter a list of lowercase integers
visible_colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for i in range(len(visible_colors)):
    visible_colors[i] = visible_colors[i][0].upper() + visible_colors[i][1::]

print(visible_colors)
```

</p>
</details>

## While loops

While loops are used when your loop could run an indeterminate number of times. Think of it like when a recipe has instructions like this, "While the bread isn’t brown, keep cooking". While loops checks if something is True (the bread isn’t brown yet) and runs until it’s set to False (now the bread is brown, so stop).

```python
# While <a condition is true>:
#     Run some code
#     Change something about the conditional statement

a = 0
while a < 10:
  print(a)
  a += 1
```

**Be wary of infinite loops**, if you don't change something about the statement in the while loop, it'll run forever, thus never reaching the code that follows it.
