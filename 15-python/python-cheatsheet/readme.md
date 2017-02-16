# Python Cheatsheet
Here's a collection of some useful pieces of Python code. This cheatsheet
is designed to help you quickly look up how to do common, useful things
and hopefully it clears up confusion about problems you may run into:

Also, here's a great external reference that provides an excellent list of
tips and tricks in Python. Lots of the tips are great and you'll use right
away. Some tips relate to advanced material or features that we won't use.
Simply ignore anything that isn't immidiately beneficial to you.

[30 Essential Python Tips and Tricks](http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1)

### Numbers
Force integer division with `//`
```python
2 / 3   # .6666666666
2 // 3  # 0

3 / 2   # 1.5
3 // 2  # 1
```

Import the `random` library to gain access to all sorts of nice methods.
Choose a random float number from 0.0 up to but not including 1.0.

Choose an integer from 2 up up and including 10.

```
import random

random.random()
random.randint(2,6)
```

### if / else if / else Statements
Python uses silly spellings for "else if". Write it as `elif`.

```
import random

barrel = random.randint(1,6)
if n == 1:
  print("BANG!")
elif n == 2:
  print("click. phew. that was close.")
else:
  print("click")
```

### User Input
Write programs that allow users to type in input from the terminal.
Everything the user inputs is returned as a string. Use the `int`
function to convert it to an integer.

```python
name = input("What's your name? ")
count = input("How many times shall I greet you? ")
count = int(count)

for i in range(count):
  print(f"Hello {name}!")
```

### Multiple Variable Assignment!
Ever have an array, or two variables and try to swap them, then find out that
one value stomped the other? Python's got your back.

Classically you would need to use a third variable as a temporary variable
to store one value while the second value overwrites the first.

```python
foo = "ace"
bar = "king"

temp = bar
bar = foo
foo = temp
```

Python supports multi-variable assignment. If you have N variables on the left
side of an equals sign, and N values on the right side then Python automatically
unpacks the values and stores them in the two variables simultaneously.

```python
foo = "ace"
bar = "king"

foo, bar = bar, foo

a = [12, 42]
a[0], a[1] = a[1], a[0]
```

### Strings
Strings have some different method names than JavaScript. Remember to use
`len()` to find out the length of something.

Fire up the `ipython3` shell to play with things and see what they have.
Create a variable `s` equal to any string value, then types `s.` and press TAB
to have the ipython shell prompt you with useful auto-complete method names.

```python
In [1]: s = ""
In [2]: s.
         s.capitalize   s.format       s.islower      s.lower        s.rpartition   s.title
         s.casefold     s.format_map   s.isnumeric    s.lstrip       s.rsplit       s.translate
         s.center       s.index        s.isprintable  s.maketrans    s.rstrip       s.upper
         s.count        s.isalnum      s.isspace      s.partition    s.split        s.zfill
         s.encode       s.isalpha      s.istitle      s.replace      s.splitlines
         s.endswith     s.isdecimal    s.isupper      s.rfind        s.startswith
         s.expandtabs   s.isdigit      s.join         s.rindex       s.strip
         s.find         s.isidentifier s.ljust        s.rjust        s.swapcase
```

Strings support awesome Python "slice notation."

```python
s = "faced"
s[0]     # "f" first letter
s[-1]    # "d" last letter
s[:-1]   # "face" everything up to the last letter
s[1:]    # "aced" everything after the first letter
s[::2]   # "fcd" every other letter
s[::-1]  # "decaf" the string in reverse
s[1:-1]  # "ace" the middle of the string between first and last letter
```

Don't forget about `f-strings` for their awesome formatting potential!

```python
name = "Sean Nelson"
city = "Seattle"
msg = f"{name} lives in the city of {city}."
print(msg) # "Sean Nelson lives in the city of Seattle."
```

### Lists
Lists (arrays) also support the same slice notation!

```python
a = [11, 42, 53, 65, 99]
a[0]    # 11
a[-1]   # 99
a[::2]  # [11, 53, 99]
a[::-1] # [99, 65, 53, 42, 11]
```

Use the `for foo in bar:` syntax to iterate through every item with a
for each loop.

```python
bar = [11, 42, 53, 65, 99]
for foo in bar:
  print(foo)
```

Use the `enumerate` function to count the items as they pass through the
for each loop.

```python
bar = [11, 42, 53, 65, 99]
for i, foo in enumerate(bar):
  print(f'{foo} is at index {i}')
```

Use the `range` function if you just want to make a for loop that counts
up to something. Iterating over a range with a for loop is a convenient
way to get access to an `i` variable that you want to interact with.

Range takes integers for `min`, `max` and `step` to determine where to
start, where to end, and how big of a step to take each time.

Run a for loop that starts at 1 and goes to the end of the length of the
array. Starting at 1 guarantees that we'll be able to safely access the
zero index and never exceed the length of the array.

```python
a = [1,7,4,3,2]
for i in range(1, len(a)):
  if a[i - 1] > a[i]:
    print(f"yes: {a[i-1]} is greater than {a[i]}")
  else:
    print(f" no: {a[i-1]} is not greater than {a[i]}")
```

Create an array of fixed size. Create an array from a range of
numbers. The `range` function excludes so we add one. Also, `range`
doesn't return a list itself, so we pass it to the `list` function
to convert the sequence it returns into an actual list.

```python
ten_item_array = [0] * 10
one_through_ten = list(range(1, 10 + 1))

print(ten_item_array)   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(one_through_ten)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Dictionaries (or hash maps, or "javascript objects")
Python is picky about the key value. If the key value is a string then
it must be wrapped in quotation marks. Because, you know, it's a string.

Access key/value pairs with brackets. Use a for loop to iterate over the
keys in a dictionary and use that key to access the values.

```python
dd = {
  "name": "Sean Nelson",
  "city": "Seattle",
}

dd["name"]   # "Sean Nelson"
dd["city"]   # "Seattle"

for key in dd:
  print("key:", key)
  print("val:", dd[key])
  print()
```

The for loop above prints out:

```
key: name
val: Sean Nelson

key: city
val: Seattle
```

If you try to access a dictionary at a key that doesn't exist then the program
will crash and you'll see an error:

```
dd["invalid"]

----------------------------------------------
KeyError     Traceback (most recent call last)
<ipython-input-20-2bc5d4d8169e> in <module>()
----> 1 dd["invalid"]

KeyError: 'invalid'
```

The `defaultdict` from the standard `collections` library is a very useful dictionary
implementation that can be configured to prevent that nasty `KeyError` and return
a default value.

Let's say we want to count up letters in a string. We'll use a dictionary to map
letter -> count pairs. Each letter has it's own count. The `defaultdict` allows
us to express, "if the key isn't in the dictionary then return an integer".

You need to import the defaultdict from the collections library to use it.

```python
from collections import defaultdict

dd = defaultdict(int)
ss = "here is a sentence with probably a lot of eeeees"
for letter in ss:
  dd[letter] += 1

print(dd)
```

That code prints out something like this:

```
{ 'h': 2, 'e': 10, 'r': 2,
  ' ': 9, 'i': 2, 's': 3,
  'a': 3, 'n': 2, 't': 3,
  'c': 1, 'w': 1, 'p': 1,
  'o': 3, 'b': 2, 'l': 2,
  'y': 1, 'f': 1}
```
