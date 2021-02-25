# Intro to Classes

## Objectives
* Understand difference between objects and classes
* Understand how classes are defined
* Understand how objects are initialized
* Understand instance variables and instance methods
* Understand class variables and class methods
* Utilize the `self` keyword
* Understand method chaining in a class

# Classes
Python is an object-oriented language. Object-oriented languages allow us to
create things that act like physical objects in our day-to-day lives. Every day
we interact with objects like chairs, beverages, and CDs. These objects have
properties that define them, and they have things we can do with them.

A **class** is like a **blueprint** for an object. It isn't an actual object in and of itself; it's simply a set of instructions for how to build a particular type of object, and how it should function.

A builder can take a blueprint for a house and build as many instances of that blueprint as they want. Similarly, if I programmer has a class, they can create multiple **instances** of that class. 

## Example: CoffeeCup

Let's write a `CoffeeCup` class that has the following properties:
* capacity (how much coffee can it hold)
* amount (how much is it currently holding)
* fill (to fill the cup to it's max capacity with coffee)
* empty (to rid the cup of any existing coffee by drinking it all or pouring it out)
* drink (to drink some amount of the coffee that is currently in the cup)

Classes are made of variables and methods. In this case we have:
* Variables: capacity, amount
* Methods: fill, empty, drink

### Constructor

Every class needs a **constructor**, which is a special method that is used to construct instances of the class. In python, the constructor is the `__init__` method, which is where all the initial values of the variables are set.

In the cass of our `CoffeeCup` class, we have two variables that need to be set:
* capacity - this can vary from cup to cup, so we'll need to have the programmer set this initial value on each instance
* amount - this presumably starts at zero upon creation of the cup

`__init__` takes `self` as the first parameter always. This is how python keeps track of binding (similar to `this` in javascript). Any variables that do not have a standard initial value (like `capacity` in this case), can be initialized through the parameter list of the constructor. This is what our `CoffeeCup` class looks like with a constructor: 

```python
class CoffeeCup():
  def __init__(self, capacity): # constructor
    self.capacity = capacity
    self.amount = 0
```
The `CoffeeCup` is a collection of variables and methods. The variables in
this class are `self.capacity` and `self.amount` and they are initialized by the constructor. 

### Creating Instances

A constructor is actually all you need to create an object! Create instances of a class by calling `ClassName()`. This invokes the
`__init__` method. You can pass parameters to it too, `ClassName(param1, param2)` (in this case, capacity). We treat the constructor as if the `self` parametee isn't there - python handles this bit for us.

```python
nicks_cup = CoffeeCup(12)  # a fancy latte.
daves_cup = CoffeeCup(16)    # gas station drip.
taylors_cup = CoffeeCup(2)  # a quick espresso.
```

### Printing Objects

Let's try printing a cup:

```python
print(nicks_cup)
```

What happens?

```
<__main__.CoffeeCup object at 0x7f68e63f5820>
```

This nasty output is showign us what type of an object it is, and a number representing something about where the object exists in memory, which we don't care about. We can override this default by explicitly writing a `__str__` method (which stands for 'stringify'... or something like that):

```python
class CoffeeCup():
	def __init__(self, capacity):
		self.capacity = capacity
		self.amount = 0
	
	def __str__(self):
		return 'This {}oz coffee cup is {}oz full.'.format(self.capacity, self.amount)
```

`__str__`, like `__init__` is a special method that must be named exactly this. Try printing Nick's cup again!


### Adding Methods

Nick needs some coffee in his cup, so we need a way to fill it! We can add a `fill` method like so:

```python
class CoffeeCup():
	def __init__(self, capacity):
		self.capacity = capacity
		self.amount = 0
	
	def __str__(self):
		return 'This {}oz coffee cup is {}oz full.'.format(self.capacity, self.amount)
	
	def fill(self):
		self.amount = self.capacity
```

Now let's see Nick's cup before and after filling:

```python
print(nicks_cup)
nicks_cup.fill()
print(nicks_cup)
```

Now let's add a `drink` method. We'll take in an `amount` parameter to this method so we know how much coffee to remove:

```python
	def drink(self, amount):
		self.amount -= amount
		if(self.amount<=0):
			self.amount=0
```

To test, fill Dave's cup, then have him drink 10oz:

```python
daves_cup.fill()
daves_cup.drink(10)
print(daves_cup)
```

Let's say Dave is REALLY needing some get-up-and-go so he takes *another* 10oz gulp (test the edge case):

```python
daves_cup.drink(10)
print(daves_cup)
```

Looks like Dave needs a refill!

***Exercise:*** Now try adding an `empty` method on your own and test it.

---

### Final Code from CoffeeCup code-along

```python
class CoffeeCup():
	def __init__(self, capacity):
		self.capacity = capacity
		self.amount = 0
	
	def __str__(self):
		return 'This {}oz coffee cup is {}oz full.'.format(self.capacity, self.amount)
	
	def fill(self):
		self.amount = self.capacity
	
	def drink(self, amount):
		self.amount -= amount
		if(self.amount<=0):
			self.amount=0

nicks_cup = CoffeeCup(12)  # a fancy latte.
daves_cup = CoffeeCup(16)    # gas station drip.
taylors_cup = CoffeeCup(2)  # a quick espresso.

print(nicks_cup)
nicks_cup.fill()
print(nicks_cup)
daves_cup.fill()
daves_cup.drink(10)
print(daves_cup)
daves_cup.drink(10)
print(daves_cup)
```

---

## Default Parameters
Python allows us to provide default values for parameters in any function we
provide. Let's write a `Point` class that has `x` and `y` variables. If no
`x` and `y` values are provided when a `Point` is initialized `x` and `y`
should both default to zero.

```
class Point():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
```

Add a method called `distance` that calculates and returns the distance between
the current point and the origin. Use the mathematical distance formula where
the distance between a point and the origin is defined as the square root of
(x*x + y*y).

Use Python's math module by adding `import math` at the top:

```python
import math

class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def distance(self):
		return math.sqrt(self.x**2+self.y**2)
```


**OR** leverage the fact that the square root of a number is equivalent to raising that number to the 1/2

```
  def distance(self):
    return (self.x ** 2 + self.y ** 2) ** .5
```

Test it:

```
p0 = Point()
p2 = Point(3, 4)

print(p0.distance())
0.0

print(p2.distance())
5.0
```

---

## Exercise: Create Your Own Class
Write a `BankAccount` class.
* Upon creation, accounts should have a type (like savings, or checking).
* Upon creation, accounts should have a `balance` that can be set to a specific amount or default to `0`.
* Each account should have access to a `deposit` method that adds a certain amount to the balance.
* Each account should have a `withdraw` method that subtracts a certain amount from the balance and returns that amount
* When an account is printed, it should show the current balancemy

Create a checking account and a savings account. Withdraw money from the savings
account and deposit that amount into the checking account.

Bonus: start each account with an additional `overdraft_fees` property that
starts at zero. If a call to `withdraw` ends with the `balance` below zero
then `overdraft_fees` should be incremented by twenty. Overdraft fees should show when the account is printed.

---

### Bank Accounts Solution

```python
class BankAccount():
	def __init__(self, acct_type, balance=0):
		self.type = acct_type
		self.balance = balance
		self.overdraft_fees = 0
	
	def __str__(self):
		status = 'balance: {} \noverdraft fees: {}'.format(self.balance, self.overdraft_fees)
		return status
	
	def deposit(self, amount):
		self.balance += amount
	
	def withdraw(self, amount):
		self.balance -= amount
		if (self.balance < 0):
			self.overdraft_fees += 20
		return amount

my_acct = BankAccount('checking', 6)
my_acct.deposit(50)
my_acct.withdraw(25)
print(my_acct)
my_acct.withdraw(35)
print(my_acct)
```

---

## Class Variables
In our examples so far, each class has variables attached to the `self` property that exist independently for each object that's created. We can also attach variables to the class itself so that there's one single thing that exists for an entire class. These are called **class variables**.

For the `Point` class we'll create a class variable to represent `ORIGIN`. Class variables are available even without creating any instances of a class. We'll be able to write code that references `Point.ORIGIN` by itself.

Change the `distance` method to accept a reference to a second Point as an optional parameter. The second point parameter should have a default value of `None`. The distance formula between two points is the square root of the difference between the two x coordinates (dx) squared, plus the difference between the two y coordinates (dy): `sqrt(dx^2 + dy^2)` 

```python
  def distance(self, p2=None):
    dx = self.x - p2.x
    dy = self.y - p2.y
    return sqrt(dx ** 2 + dy ** 2)
```

We will write an `if` statement to detect when p2 is `None` and set it to `Point.ORIGIN` instead.

It's hard to reference the `Point` class in the class definition itself because it hasn't finished being created yet. We'll attach `ORIGIN` to the `Point` class after it's defined.

```python
class Point():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "({},{})".format(self.x, self.y)
  
  def distance(self, p2=None):
    if p2 is None:
      p2 = Point.ORIGIN
    dx = self.x - p2.x
    dy = self.y - p2.y
    return sqrt(dx**2 + dy**2)

# attach ORIGIN after the Point class is defined
Point.ORIGIN = Point()
```

```python
# we can access ORIGIN through the Point class.
print(Point.ORIGIN)
(0,0)

p1 = Point(3,4)
p2 = Point(3,19)

# Distance defaults to calculating how far away a Point is from ORIGIN
p1.distance()
5.0

# Distance will calculate the distance from one point to another if a
# a second Point is provided as a parameter.
p1.distance(p2)
15.0
```

# Final Thoughts
Classes are an excellent example of how the Python programming language has
benefitted from thorough design and community development. JavaScript was first
created in 10 days by one person. Creating classes in JavaScript is a total
pain. JavaScript is only recently gaining full-fledged, easy-to-use
Object Oriented programming features that Python has had for a long time.
