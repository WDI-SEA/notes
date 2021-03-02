# Inheritance in Python

## Objectives
* Implement inheritance
* Describe what has been inherited from one class to another
* Identify inheritance syntax
* Use inheritance to reduce repetition
* Use inheritance to model the world

### Review
1. What is a method?
2. What is a class?
3. What is an instance method?
4. Why do we use a class?

# Inheritance
To avoid reinventing the wheel, we can write **sub-classes** aka **child classes** that **inhehrit** the properties of their **super class** (aka **parent class**). You've actually already seen this if you've written a class-based React component that starts with `class Something extends React.Component`. The componente (i.e. the class) you're writing inherits lots of properties from a superclass supplied by React, which has things like state, lifecycle methods, etc.

## Super Class: Phone 

Let's dive into an example. We'll a **Phone** class, then some sub-classes of **Phone**, namely **IPhone** and **AndroidPhone**. 

All phones 
* have a phone number
* can place phone calls
* can send text messages

Write a **Phone** class that has a `number` property, a `__str__` method, as well as `call` and `text` methods:

```python
class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def __str__(self):
        return str(self.number)

    def call(self, other_number):
        print("Calling {} from {}.".format(self.number, other_number))

    def text(self, other_number, msg):
        print("Sending text from {} to {}:".format(self.number, other_number))
        print(msg)
```

```
1111111111
2222222222
Calling 1111111111 from 2222222222.
Sending text from 2222222222 to 1111111111:
hello, world
```
Try making some phone instances and calling their methods!

---
## Sub-classes: Iphone & AndroidPhone

Let's define two new classes that `inherit` from the **Phone** class.
We'll make an **IPhone** and an **AndroidPhone**.

### Iphone

First thing we need when creating a sub-class is to pass it the parent class:
```python
class IPhone(Phone):
```

Next, we call the parent constructor and pass any paremeters from the parent constructor into it:

```python
class IPhone(Phone):
  def __init__(self, phone_number, generation, color):
    super().__init__(phone_number)
    self.generation = generation
    self.color = color
```

Create an instance of IPhone and verify that it inherited all the same functionality of the Phone class: 

```Python
iPhone3 = IPhone(3333333333, '7s', 'black')
print(iPhone3)
iPhone3.call(phone2)
phone1.text(iPhone3, 'im so fancy')
```

```
3333333333
Calling 3333333333 from 2222222222.
Sending text from 1111111111 to 3333333333:
im so fancy
```

You can overwrite methods from the superclass by simple redefining it in the sub-class. For example, let's write a `__str__` method for IPhone and see what happens:

```python
class IPhone(Phone):
    def __init__(self, phone_number, generation, color):
        super().__init__(phone_number)
        self.generation = generation
        self.color = color
    
    def __str__(self):
        return(f'{self.generation} {self.color} Iphone {self.number}')

iPhone3 = IPhone(3333333333, '7s', 'black')
```

iPhones have that cool/scary fingerprint functionality now - let's make our IPhone class mimic this behavior, by adding a `set_fingerprint` method, as well as an `unlock` method.

1. Add a `fingerprint` property to the constructor that initializes to `None`
2. `set_fingerprint`: takes a fingerprint and sets it to the instance's `fingerprint` property
3. `unlock`: accepts a fingerprint and and compares it to the stored fingerprint for that instance. If there is no stored fingerprint, or if the input fingerprint doesn't match the stored fingerprint, do not unlock. Otherwise, unlock
    
```python
class IPhone(Phone):
    def __init__(self, phone_number, generation, color):
        super().__init__(phone_number)
        self.generation = generation
        self.color = color
        self.fingerprint = None
    
    def __str__(self):
        return(f'{self.generation} {self.color} Iphone {self.number}')
    
        self.fingerprint = None
    
    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint
    
    def unlock(self, fingerprint=None):
        if (not self.fingerprint):
            print("Phone unlocked because the fingerprint has not been set.")
        elif (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")
```
```python
iPhone3 = IPhone(3333333333, '7s', 'black')
# print(iPhone3)
# iPhone3.call(phone2)
# phone1.text(iPhone3, 'im so fancy')
iPhone3.unlock()
iPhone3.set_fingerprint('Taylor\'s thumb')
iPhone3.unlock('Dave\'s thumb')
iPhone3.unlock('Taylor\'s thumb')
```
```
Phone unlocked because the fingerprint has not been set.
Phone locked. Fingerprint doesn't match.
Phone unlocked. Fingerprint matches.
```

### Android 
* Android phones have a unique `set_keyboard` method that accepts a keyboard

```python
class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.keyboard = "Default"
    
  def set_keyboard(self, keyboard):
    self.keyboard = keyboard
```
