# Classes

## Intro to Classes

### Objectives

* Understand difference between objects and classes
* Understand how classes are defined
* Understand how objects are initialized
* Understand instance variables and instance methods
* Understand class variables and class methods
* Utilize the `self` keyword
* Understand method chaining in a class

## Classes

Python is an object-oriented language. Object-oriented languages allow us to create things that act like physical objects in our day-to-day lives. Every day we interact with objects like chairs, beverages, and CDs. These objects have properties that define them, and they have things we can do with them.

A **class** is like a **blueprint** for an object. It isn't an actual object in and of itself; it's simply a set of instructions for how to build a particular type of object, and how it should function.

A builder can take a blueprint for a house and build as many instances of that blueprint as they want. Similarly, if I programmer has a class, they can create multiple **instances** of that class.

### Example: CoffeeCup

Let's write a `CoffeeCup` class that has the following properties:

* capacity \(how much coffee can it hold\)
* amount \(how much is it currently holding\)
* fill \(to fill the cup to it's max capacity with coffee\)
* empty \(to rid the cup of any existing coffee by drinking it all or pouring it out\)
* drink \(to drink some amount of the coffee that is currently in the cup\)

Classes are made of variables and methods. In this case we have:

* Variables: capacity, amount
* Methods: fill, empty, drink

#### Constructor

Every class needs a **constructor**, which is a special method that is used to construct instances of the class. In python, the constructor is the `__init__` method, which is where all the initial values of the variables are set.

In the cass of our `CoffeeCup` class, we have two variables that need to be set:

* capacity - this can vary from cup to cup, so we'll need to have the programmer set this initial value on each instance
* amount - this presumably starts at zero upon creation of the cup

`__init__` takes `self` as the first parameter always. This is how python keeps track of binding \(similar to `this` in javascript\). Any variables that do not have a standard initial value \(like `capacity` in this case\), can be initialized through the parameter list of the constructor. This is what our `CoffeeCup` class looks like with a constructor:

```python
class CoffeeCup():
  def __init__(self, capacity): # constructor
    self.capacity = capacity
    self.amount = 0
```

The `CoffeeCup` is a collection of variables and methods. The variables in this class are `self.capacity` and `self.amount` and they are initialized by the constructor.

#### Creating Instances

A constructor is actually all you need to create an object! Create instances of a class by calling `ClassName()`. This invokes the `__init__` method. You can pass parameters to it too, `ClassName(param1, param2)` \(in this case, capacity\). We treat the constructor as if the `self` parametee isn't there - python handles this bit for us.

```python
nicks_cup = CoffeeCup(12)  # a fancy latte.
daves_cup = CoffeeCup(16)    # gas station drip.
taylors_cup = CoffeeCup(2)  # a quick espresso.
```

#### Printing Objects

Let's try printing a cup:

```python
print(nicks_cup)
```

What happens?

```text
<__main__.CoffeeCup object at 0x7f68e63f5820>
```

This nasty output is showign us what type of an object it is, and a number representing something about where the object exists in memory, which we don't care about. We can override this default by explicitly writing a `__str__` method \(which stands for 'stringify'... or something like that\):

```python
class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def __str__(self):
        return 'This {}oz coffee cup is {}oz full.'.format(self.capacity, self.amount)
```

`__str__`, like `__init__` is a special method that must be named exactly this. Try printing Nick's cup again!

#### Adding Methods

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

Let's say Dave is REALLY needing some get-up-and-go so he takes _another_ 10oz gulp \(test the edge case\):

```python
daves_cup.drink(10)
print(daves_cup)
```

Looks like Dave needs a refill!

_**Exercise:**_ Now try adding an `empty` method on your own and test it.

#### Final Code from CoffeeCup code-along

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

### Exercise: Create Your Own Class

#### Car Class

Create a class called `Car` that has the following attributes:
- `make` (string)
- `model` (string)
- `year` (int)
- `speed` (int, default value 0)

The class should have the following methods:
- `accelerate(amount)` - Increases the speed by `amount`
- `brake(amount)` - Decreases the speed by `amount`

#### Solution

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
```

## Final Thoughts

Classes are an excellent example of how the Python programming language has benefitted from thorough design and community development. JavaScript was first created in 10 days by one person. Creating classes in JavaScript is a total pain. JavaScript is only recently gaining full-fledged, easy-to-use Object Oriented programming features that Python has had for a long time.

