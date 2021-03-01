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

Let's dive into an example. We'll a **Phone** class, then some sub-classes of **Phone**, namely **IPhone** and **AndroidPhone**. 

All phones 
* have a phone number
* can place phone calls
* can send text messages

Write a **Phone** class that has a `number` property, as well as `call` and `text` methods:

```python
class Phone:
  def __init__(self, phone_number):
    self.number = phone_number
    
  def call(self, other_number):
    print("Calling {} from {}.".format(self.number, other_number))
    
  def text(self, other_number, msg):
    print("Sending text from {} to {}:".format(self.number, other_number))
    print(msg)
```


Let's define two new classes that `inherit` from the **Phone** class.
We'll make an **IPhone** and an **AndroidPhone**.

* iPhones have a unique `unlock` method that accepts a fingerprint
* iPhones have a unique `set_fingerprint` method that accepts a fingerprint
* Android phones have a unique `set_keyboard` method that accepts a keyboard

    
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
