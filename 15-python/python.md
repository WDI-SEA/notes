# Python Daily Mini-Surveys
Let us know how Python is going. Fill this thing out every day:

<https://docs.google.com/forms/d/e/1FAIpQLSdP64Gw64ZI5Z1LK01MLoHym2jXBuguoYlGvqPsqaPHF4xkqA/viewform>

#Python
Python is a widely used high-level programming language used for general-purpose
programming, created by Guido van Rossum and first released in 1991. Python has
a design philosophy which emphasizes code readability. You'll often find that
your first guess at what a function is called is surprisingly correct.

For instance, if you want to print something, you write:

```python
print("I'm not dead yet!")
```

Also, it's true. Python's name is derived from Monty Python.

## Python Console
Python has an interactive console you can use in your terminal. Type `python3`
to get started.

Note: there are two versions: Python2 and Python3. We'll be using Python3.
If you ever type simply `python` in the terminal the terminal will assume you
mean Python2. Python3 is better.

## Philosophy
The core philosophy of Python is summarized by the document
[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
, which includes aphorisms such as:

* Beautiful is better than ugly
* Explicit is better than implicit
* Simple is better than complex
* Complex is better than complicated
* Readability counts

## Familiar Datatypes
Python has all the data types you're used to using in JavaScript. Python
has variables, functions, booleans, integers, floats, strings, lists and
dictionaries (objects). You never declare `var` in Python.

This is all legal Python:

```python
my_name = "Steve"
my_age = 2017 - 1988
is_alive = True
my_hobbies = ["board games", "programming", "bikes"]

person = {
  "name": my_name,
  "age": my_age,
  "hobbies": my_hobbies,
}

print(person)
print(person["name"], "has", len(person["hobbies"]), "hobbies.")
```

## Negative String Indexes!!
Python has some little features that make code really sweet to write. Negative
string (and array) indexes is simply one example of great syntax options Python
offers.

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

# we can use negative numbers to access characters in a string from backwards!
last_letter = alphabet[-1]
third_to_last_letter = alphabet[-3]
print(last_letter, "is the last letter in the alphabet")
print(third_to_last_letter, "is the third to last letter in the alphabet")

# we can use the `in` keyword to see if something is part of a string!
if ("e" in vowels):
  print("yup. that's a vowel.")
```

## Whitespace
Python never uses curly braces to define blocks of code. Instead, it forces
programmers to write their code with proper whitespace. Many people find this
annoying and you're bound to hear people scoff at Python for this decision.

Here's what a for loop and an if else statement look like in Python. The
whitespace is important! You have to consistently indent with tabs, or spaces.
Whichever you choose you have to be consistent with how many tabs or spaces you
use at each level!

Notice that Python uses a weird word `elif` for "else if" statements.

```python
for i in range(1, 18):
  if i % 3 == 0 and i % 5 == 0:
    print("divisible by three and five")
  elif i % 3 == 0:
    print("divisible by three")
  elif i % 5 == 0:
    print("divisible by five")
  else:
    print(i)
```

## Functions
Python allows you to define functions with parameters. Parameters can even be
declared with default values in case you want to call a function without passing
in parameters:

```python
def greet(name="Mysterious Stranger"):
  print("Hello there", name)

greet("Bruce Wayne")
greet()
```

## For Loops
There's no `for (var i = 0; i < a.length; i++)` for loops in Python. All for
loops in Python use automatic iterators, like this:

```python
# traditional for loop
for i in range(0,10):
  print(i)

# backwards for loop, where it goes down by negative one at each step.
for i in range(10, 0, -1):
  print(i)

# a for loop going from 0 to 100 incremented by 17 at each step.
for i in range(0, 100, 17):
  print(i)
```

Python comes with lots of built in libraries. We're able to import all sorts
of useful tools.

Ever wanted to shuffle an array?

```python
import random

cards = ["Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight"]
print("Original Deck:", cards)
random.shuffle(cards)
print("Shuffled Deck:", cards)
```

Ever wanted to choose one random thing from a list?

```python
import random

print("Where should I move?")
cities = ["Seattle", "Portland", "San Francisco", "Vancouver"]
city = random.choice(cities)
print("That's it. I'm moving to", city)
```

That's just a small taste. Let's see what else Python has to offer!
