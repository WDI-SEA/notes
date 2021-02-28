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
Inheritance allows us to build new classes out of old classes.
It allows us to extend functionality defined in a `parent`
class and create `children` classes that extend and
compartmentalize different pieces of functionality.

Inheritance models natural hierarchies that we're used to
thinking about in the world. We can define one general class
to model something like an **Phone** and then `inherit` the
methods and properties of the class to make new classes out of
the first class, like **IPhone** and **AndroidPhone**.

When we say sub-classes, or child classes, `inherit` methods
and properties from a parent class we mean the child class
has access to all of the functionality of it's parent, and
it can define it's own functionality on top of that.

When we define a class to represent a **Phone** we can add
the basic properties and functionality that all phones
have.

* All phones have a phone number
* All phones can place phone calls
* All phone can send text messages

After we define what a **Phone** is we can create classes
that `inherit` from the Phone class and add their own
properties and functionality.

Let's define two new classes that `inherit` from the **Phone** class.
We'll make an **IPhone** and an **AndroidPhone**.

* iPhones have a unique `unlock` method that accepts a fingerprint
* iPhones have a unique `set_fingerprint` method that accepts a fingerprint
* Android phones have a unique `set_keyboard` method that accepts a keyboard

```python
class Phone:
  def __init__(self, phone_number):
    self.number = phone_number
    
  def call(self, other_number):
    print("Calling {} from {}.".format(self.number, other_number))
    
  def text(self, other_number, msg):
    print("Sending text from {} to {}:".format(self.number, other_number))
    print(msg);
```
    
```python
class IPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number):
    self.fingerprint = None
    
  def set_fingerprint(self, fingerprint):
    self.fingerprint = fingerprint
    
  def unlock(self, fingerprint=None):
    if (fingerprint == self.fingerprint):
      print("Phone unlocked because no fingerprint has not been set.")
      
    if (fingerprint == self.fingerprint):
      print("Phone unlocked. Fingerprint matches.")
    else:
      print("Phone locked. Fingerprint doesn't match.")
  
class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.keyboard = "Default"
    
  def set_keyboard(self, keyboard):
    self.keyboard = keyboard
```

## Inheritance Syntax
There's two new pieces of syntax used in the code above.

* Class definitions can accept a parameter specifying what class they inherit
  from.
* Child classes can invoke a method called `super()` to gain access to
  methods defined in the parent class and execute them.
  
Take another look at the Phone classes to see how these pieces of syntax
are used to define how the classes define their inheritance and how the
`super()` method is used.

Notice how the Android class doesn't repeat the code that attaches the
phone_number passed to the `__init__` method to the `self` reference. The
Android class calls the parent constructor through the super method and
allows the parent class to execute that default behavior.
  
```python
class Parent:
  def __init__(self, phone_number):
    self.phone_number = phone_number
    
class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
```

## Exercise: Write Bank Account Classes
Let's practice writing classes and using inheritance by modelling different types
of Bank accounts.

* Create a base **BankAccount** class
  * Bank accounts keep track of their current `balance`
  * Bank accounts have a `deposit` method
  * Bank accounts have a `withdraw` method
  * the `deposit` method returns the balance of the account after adding
    the deposited amount.
  * the `withdraw` method returns the amount of money that was successfully
    withdrawn.
  * Bank accounts return `False` if someone tries to deposit or withdraw
    a negative amount.
  * Bank accounts are created with a default interest rate of 2%
  * Bank accounts have a `accumulate_interest` method that sets the balance
    equal to the balance plus the balance times the interest rate
  * `accumulate_interest` returns the balance of the account after calculating
    the accumulated interest
* Create a **ChildrensAccount** class
  * Children's bank accounts have an interest rate of Zero.
  * Every time `accumulate_interest` is executed on a Child's account the
    account  always gets $10 added to the balance.
* Create an **OverdraftAccount** class
  * An overdraft account penalizes customers for trying to draw too much
    money out of their account.
  * Overdraft accounts are created with an `overdraft_penalty` property
    that defaults to $40.
  * Customer's aren't allowed to withdraw more money than they have in their
    account. If a customer tries to withdraw more than they have then the
    withdraw method returns `False` and their balance is deducted only by
    the amount of the `overdraft_penalty`.
  * Overdraft accounts don't accumulate interest if their balance is below zero.
    
Sample Input:
```python
basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
```

Sample Output:
```
Basic account has $600
Basic account has $583
Basic account has $594.66

Child's account has $34
Child's account has $17
Child's account has $27

Overdraft account has $12
Overdraft account has $-28
Overdraft account has $-28
```
