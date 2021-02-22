# Python
Python is a widely used high-level programming language used for general-purpose
programming, created by Guido van Rossum and first released in 1991. Python has
a design philosophy which emphasizes code readability. You'll often find that
your first guess at what a function is called is surprisingly correct.

For instance, if you want to print something, you write:

```python
print("I'm not dead yet!")
```

Also, it's true. Python's name is derived from Monty Python.

## Philosophy
The core philosophy of Python is summarized by the document
[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
, which includes aphorisms such as:

* Beautiful is better than ugly
* Explicit is better than implicit
* Simple is better than complex
* Complex is better than complicated
* Readability counts

## What's New?

Python is _just like javascript with slightly different syntax_. There are very few **major** differences between Python and Javascript, but here are a few things that will be new:

### Negative String Indexes!!
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

### Whitespace
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
