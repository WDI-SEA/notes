# Python Crash Course: Features and Syntax!

Here's the long list of how to get Python to do the things you already know how
to do in JavaScript. Let's dive right into it.

## Comments

In Python, multiline comments exist, but we generally use line comments with hashtags, for readability.
```python
# here is a line comment

# here is a block
# of comments
# for you to read
```

For multiline comments in Python, you can use `"""` blocks. However observe proper indentation or you will get a `SyntaxError`.

## Variables

Local variables start with a lowercase letter. No `var` necessary. Most Python
programs choose to insert underscores between words instead of writing names in
camelCase (this is considered more readable by the PEP maintainers). 

```python
my_variable = 5
print(my_variable)
```

## Data Types

### Nothingness
Just as Javascript uses undefined or null, Python uses `None`.

`None` is a unique datatype (`NoneType`) and is not equivalent to `False`, empty string, or `0`. However, `None` does not evaluate to `True`.

```python
my_bank_account = None

if my_bank_account:
   print("This is true!")
else:
   print("This is not true...")
   
# will print "This is not true..."
```

### Booleans
A binary representation: either `True` or `False`. Capitalization matters here.
you must write "True" and Python will not recognize "true."

```python
is_operating = True
is_broken = False
```

### Numbers
There are several datatypes used to represent numbers:

* int: `23`
* float: `0.8947368421052632`
* complex: `2+3j`

Python does decimal division normally with `/` but you can force it
to do integer division with `//`:
```python
15 / 5.0
3.0
15 / 5
3.0

15 / 6
2.5
15 // 6
2
```

Complex numbers can be added to complex numbers:
```python
complex = 1+2j + 5 + 3j # evaluates to (6+5j)
```

Python is great at dealing with very large integers. Use `**` to
calculate exponents. JavaScript will only approximate large numbers
with Scientific Notation:

```js
// JavaScript
Math.pow(2, 999)
5.357543035931337e+300
```

```python
# Python
2 ** 999
5357543035931336604742125245300009052807024058527668037218751941851755255624680612465991894078479290637973364587765734125935726428461570217992288787349287401967283887412115492710537302531185570938977091076523237491790970633699383779582771973038531457285598238843271083830214915826312193418602834034688
```

### Strings
You can declare strings in Python just like in JavaScript:

```python
card1 = "ace of spades"
card2 = "king of hearts"
```

#### String Methods
Python has some familiar String methods like `split`. Other String
methods are under different names:

```python
"ace of spades".split(" ")
['ace', 'of', 'spades']

"abcde".split("")

"qqxzzz".index("x")
2

"boo".upper()
"BOO"

"WHY???".lower()
"why???"

"then I went to the store I like".replace("I", "you")
'then you went to the store you like'
```

You can use the special `in` keyword to quickly find out if one string
appears in another.

```python
"eggs" in "green eggs and ham"
True
```

Use the `len()` operator on a string to find it's length.

```python
len("Hawaii")
6
```

## Ranges
Python has a very cool syntax to select things inside a range. You can select a
letter in a string a specific index. You can select letters between a start and
and index. You can select letters counting backwards from the end using negative
numbers. You can select every N letters by specifying a step size.

* `str[index]` choose one letter at index
* `str[-index]` choose letter at index counting backwards from the end.
* `str[start:end]` get a range of letters from a start to end.
* `str[start:end:step]` get a range of letters taking `step` sized steps between.
* `str[:end]` omit the start index and grab letters from zero up to `end`.
* `str[start:]` omit the end index and grab letters from `start` up to the end of the string.
* `str[::-1]` reverses a string by going backwards with a step of -1 from start to end.

```python
# get the last letter
"my code rulez"[-1]
"z"

"my code rulez"[3:7]
"code"

"my code rulez"[:2]
"my"

"my code rulez"[3:]
"code rulez"

"my code rulez"[::-1]
"zelur edoc ym"

# take every other letter
"peiege eleaeteiene"[::2]
'pig latin'
```

## Arithmetic Operators
Python uses common operators for math.

```python
+
-
/    # decimal division       4 /  3 == 1.333333
//   # force integer division 4 // 3 == 1
*
**   # exponent  2 ** 3 == 27
%    # modulo    17 % 5 == 2

+=
-=
*=
/=
**=
```

## Logical Operators
Python uses `==` for equality. It uses `!=` for "not equal to." It uses the literal
words `not`, `or` and `and` instead of `!`, `||` and `&&` like JavaScript does.

```
==
!=
not
or
and
```

### Lists
Arrays in Python are called Lists.

Python lists can be indexed just like strings. Also, use the
`len()` operator to find the length of a list. Python lists don't have a
`.length` property on them.

Python lists can be indexed just like Python strings. You can use negative indexes
and select a range of values in the middle of the list.

*several ways to create an array*

```python
arr = [1,2,3]
[1,2,3]

len(arr)
3

five_zeroes = [0] * 5
[0, 0, 0, 0, 0]

len(five_zeroes)
5

five_trues = [True] * 5
[True, True, True, True, True]

last_item = ["Washington", "Oregon", "California"][-1]
"California"

# generate a range from 1 to 10 and create list out of it.
one_through_ten = list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### List Methods

```python
a = [1, 23, 12, 99, 82]
a.sort()
[1, 12, 23, 82, 99]

# reverse the list
a = a[::-1]
[99, 82, 23, 12, 1]

a.append(42)
[99, 82, 23, 12, 1, 42]

result = a.pop() # the first value is stored in the variable

# notice: the value is actually removed from the array
print(a)
[82, 23, 12, 1, 42]

# insert a value at a specific index
a.insert(0, 123)
[123, 82, 23, 12, 1, 42]

a.insert(2, 66)
[123, 82, 66, 23, 12, 1, 42]


if 42 in a:
  print("yup! it's in there.")
```

Fire up the interactive Python console on your terminal with `python3` or
`ipython3` and pass list to the help function to read documentation about
all of the methods on list.

```python
help(list)
```

### Dictionaries
Python stores key-value pairs (like objects in JavaScript) in Dictionaries.
The syntax is almost exactly like objects in JavaScript.

Anything can be used as a key. Strings are commonly used as keys. If the key is
a string then you must surround the key in quotes when the dictionary is defined.

```python
cat = {
  "name": 'Hamlet',
  "breed": 'American Shorthair',
  "fav_food": 'Prosciutto'
}

cat["name"]
'Hamlet'

cat["fav_food"]
'Prosciutto'
```

### Type Conversion
You can turn one Python data type into another by passing it to type functions:

```python
int("42")
42

str(42)
"42"

float(42)
42.0

bool(42)
True

bool(0)
False

bool("foo")
True

bool("")
False
```

## String Interpolation
Python has super convenient ways to format strings on the fly. You'll never
have to bother with crazy string concatenation again. These are like small
rendered templates.

Define any string with the letter `f` in front of the quotes and Python will
treat it as a "formatted" string. Formatted strings use curly braces `{}` to
identify where to evaluate values inside a string. The value inside the curly
braces can be variable names, or expressions.

The curly braces and the format function can refer to names for where values
appear in the template, and what values are named.

```python
state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}th state to join the union in {year}."
```

Let's see format strings calling a function too!

```python
def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)
```

F-strings are awesome. There's also a `format()` function on all strings. You can
specify empty curly braces and pass values as parameters and the parameter values
will fall in line in the order the curly braces appear.

```python
template = "My name is {} and I like {}"
template.format("Steve", "Cheese")
'My name is Steve and I like Cheese'
```

The `format()` function an also name the curly braces and accept named parameters:

```python
template = "My name is {name} and I like {food}"
template.format(food="Cheese", name="Steve")
'My name is Steve and I like Cheese'
```

## Control flow

* Conditionals

```python
vip = True
food_place = "busy"
if (food_place == "full" and not vip):
  print("Sorry, we have no room tonight.")
elif (food_place == "busy" and not vip)
  print("Please wait 10 minutes for a table.")
else:
  print("Welcome! Come sit down right away.")
```

* Loops

```python
n = 0
while n < 10:
  n++
```

```python
for i in range(0, 10):
  if i % 2 == 0:
    print("{} is even".format(i))
  if i % 2 == 1:
    print("{} is odd".format(i))
```

#### Iterating through Arrays
Python for loops always act on iterators. This means they always automatically
pull things out of a sequence and loop through those things one by one. Python
never uses a for loop where it increments a value like `i` manually.

If you want to have fine-grain control over what's happening to i, and you don't
want to just step through everything in a sequence one by one, then you're probably
better off using a while loop.

```python
foods = ["carrots", "kale", "beets"]
for food in foods:
  print("I like", food)
```

If you want access to the current index of each item then you need to pass your
list through a function called `enumerate`. Enumerate takes items out of an
iterator one by one and returns a `tuple` of the index of the item and the item
like `(index, item)`.

```python
print("My favorite foods:")
foods = ["carrots", "kale", "beets"]
for i, food in enumerate(foods):
  print("{}. {}".format(i, food))
```

`i` is still zero-indexed:

```
My favorite foods:
0. carrots
1. kale
2. beets
```

#### Iterating through Dictionaries
For loops will automatically iterate over the keys in a dictionary:

```python
car = {"wheels": 4, "doors": 2, "seats": 5}
for key in car:
  print("my car has {num} {thing}".format(thing=key, num=car[key]))

# Will print out:
# my car has 4 wheels
# my car has 2 doors
# my car has 5 seats
```

### Functions

#### In Javascript

* anonymous: `function (param1, [..param2, [...]]){...}`,
* named: `function Name(param1, [..param2, [...]]){...}`
* uses lexical scope
* used as values (functional programming)
* require explicit return
* all `params` are optional
* no default values for optional params
* functions can be used before they're declared

### In Python

* uses `def foo(param1, param2, city="Seattle"):`
* may provide default values for optional parameters
* may use one return statement to return more than one variable
* functions must be declared before they're used

#### Examples
```python
def say_hello():
  print("Hello, World!")

say_hello()
```

#### Parameters (Arguments)
```python
def say_hello(friend="Tim"):
  print("Hello, {}!".format(friend))

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie")
"Charlie is moving to Seattle, Washington"

# values passed to functions will fall in parameter order.
# parameter default values are used if nothing is passed in at that spot.
move("Charlie", "Tacoma")
"Charlie is moving to Tacoma, Washington"

move("Charlie", "Boise", "Idaho")
"Charlie is moving to Boise, Idaho"

# use names to specify exactly what parameters you're giving values to.
move("Charlie", state="Oregon")
"Charlie is moving to Seattle, Oregon"

move("Charlie", city="Boise", state="Idaho")
"Charlie is moving to Boise, Idaho"

# if you're using a named parameter, then you can mix up the order!
move("Charlie", state="Oregon", city="Portland)
"Charlie is moving to Portland, Oregon"


# Any value passed to the function will be used.
# If no value is passed for a parameter Python uses the default value
# defined in the function.
say_hello("Ronald")
say_hello("Tim")
say_hello()
```

#### Return Values
```python
def add(num1, num2):
  return num1 + num2

total = add(2, 3)
print("2 + 3 =", total)
```
#### Tuples and Multiple Return Values
Python has a datatype called a `tuple` which groups "multuple" things together.
A tuple is a collection of multiple values wrapped in parentheses. Tuples are
not lists. List support more operations than tuples. Tuples are immutable. Once
one is made it never changes. You can't add or remove things from a tuple.

Python will automatically unpack tuples into variables if the number of variables
on the left side of an equals sign is equal to the number of variables on the
right hand side.

```python
tuple = ("Fireman", "Fire Department")
job_title, office = tuple
```

Python uses tuples to return multiple values in one return statement. Here's our
own function called `divide_mod()` that allows us to calculate the division of
two numbers as well as their modulus all at once!

```python
def divide_mod(numerator, denominator):
  division = numerator // denominator
  mod = numerator % denominator
  return (division, mod)

students = 11
group_size = 4
num_groups, left_over = divide_mod(students, group_size)
msg1 = "{n} students can be divided into {m} groups of {size}"
msg2 = "with {j} students left over."

msg1 = msg1.format(n=students, m=num_groups, size=group_size)
msg2 = msg2.format(j=left_over)

print(msg1)
print(msg2)
```

```
11 students can be divided into 2 groups of 4
with 3 students left over.
```

### Input / Output
You've already seen how `print` will output information to the screen. What if
e want to accept user input? Let's try `input()`. Input takes a parameter where
we can define a message to be printed as a prompt for the input:

```python
def gather_input():
  you = input("Enter your name: ")
  friend = input("Enter a friend's name: ")
  print("Hello, {}. {} says hi.".format(you, friend))

gather_input()

# Outputs
# Enter your name: Tim
# Enter a friend's name: Bob
# Hello, Bob. Tim says hi.
```

Notice: `input()` always returns a string value. If you want someone to enter
a number then you should pass the value input returns through something like
`int()` or `float()`.

```python
age = input("how old are you?")
age = int(age)

age = int(input("how old are you?"))
```

```python
cost = input("how much was that candy bar?")
cost = float(cost)

cost = float(input("how much was that candy bar?"))
```

There's nothing special about the `int()` or `float()` functions. They try to
convert whatever value their given to an int or a float.

```
file_data = "2007,2017,Seattle"
moved_year, current_year, city = tupple(file_data.split(","))

# Convert years from strings to ints
moved_year = int(moved_year)
current_year = int(current_year)

diff = current_year - moved_year

print("Someone moved to {city} in {moved_year} and has lived there for {diff} years."
```

# Now You're Hacking!
That's a quick introduction to only some of the things Python has to offer.
You now have enough knowledge about Python's basic data types, functions, lists,
dictionaries, control flow statements to try writing some programs of our own.

Try to write a program that prompts the user for the current temperature, and
asks them whether they've entered a Celsius or Fahrenheit temperature. Have the
program convert their temperature from the units they provided into the other
units.
