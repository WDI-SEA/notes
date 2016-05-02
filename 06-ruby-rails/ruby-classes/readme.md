# Intro to Classes

##Objectives
* Understand difference between objects and classes
* Understand how objects are referenced
* Understand getters and setters
* Understand `attr_writer`, `attr_reader`, `attr_accessor`
* Understand instance variables and instance methods
* Understand class variables and class methods
* Utilize the `self` keyword
* Understand `Private`, and `Public` methods
* Understand method chaining in a class

## Class Definition of a person

Let's create our first class.

**person.rb**

```ruby
class Person

end
```

This defines a **class** definition of a `Person`. The *class* keyword denotes the *begining* of a class definition.

To create a new *instance* of our *class* we write the following:

```rb
Person.new
```

A particular instance of a *class* is a called an **object**. In general, languages that use *objects* as a primary means of *data abstraction* are said to be **Object Oriented Programming** (OOP) languages.


### Objects

What is an **object** in ruby? Basically everything that isn't a keyword.

However, this can cause you some headaches if you're not careful.

Imagine we had the following

```rb
arr1 = [1,2,3]
arr2 = arr1
arr1 << 4
#=> [1,2,3,4]
arr2
#=> [1,2,3,4]
```

Wow, the second array completely changed. That's because `arr2` was a reference to `arr1`. Both variables represented the same **object**. The way around this is to copy the object.

```rb
arr1 = [1,2,3]
arr2 = Array.new(arr1)
arr1 << 4
#=> [1,2,3,4]
arr2
#=> [1,2,3]
```

### Initialize and instance variables

In our class definition we can make use of an *initialize* method, which is run when a *new* instance of the class is created.

```rb
class Person
  def initialize
    puts "A new person was created"
  end
end
```


We can also make use of **instance variables** that are defined for each particular object and are available throughout other *methods* in the object. These variables are prefixed by an *@* symbol, i.e. `@my_var`.

```rb
class Person

  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello! My name is #{@name}."
  end
end
```


Now, when we create a new *Person* we are required to specify the `name` of the person.

```ruby
person = Person.new("John")
person.greet

=> Hello! My name is John.
```

### Getters and Setters

Having created an *instance variable* in our object, we might want to *read* that *outside* our object. However, we have to define a method that will act as an **interface for reading** for this variable called a **Getter Method**.

```ruby
class Person

  def initialize(name)
    @name = name
  end

  def name
    @name
  end

end
```

Now we can *read* or *get*  the *name* outside the object.

```ruby
person = Person.new("Jane")
person.name

=> "Jane"
```

Similarly, we may need to *change* or *set* an instance variable from outside the object, so we create a method called a **setter method**.

```ruby
class Person

  def initialize(name)
    @name = name
  end

  def name
    @name
  end

  def name=(other)
    @name = other
  end
end
```

We can now *get* and *set* the name of a person using the  methods we created for `@name`.

```ruby
person = Person.new("Samantha")
person.name

=> "Samantha"

person.name = "Sam"
person.name

=> "Sam"
```

### Getters and Setters, the Ruby way

In ruby, the practice of creating a *getter* method is so common there is a shorthand that can be used at the top of a class definition called `attr_reader`.

```ruby
class Person

  attr_reader :name

  def initailize(name)
    @name = name
  end

  def name=(other)
    @name = other
  end
end
```


Similarly, we can do the same with the *setter* method using `attr_writer`

```ruby
class Person
  attr_reader :name
  attr_writer :name

  def initialize(name)
    @name = name
  end
end
```

Moreover, we have a shorthand for telling our class to create both a *getter* and a *setter* method called *attr_accessor*.

```ruby
class Person
  attr_accessor :name

  def initialize(name)
    @name = name
  end
end
```


### Class and self

We just created instance variables, which have different values depending on the object instance. Class variables share the same value across the entire class. Also, we don't need to create an instance in order to access class variables.

Let's first create a variable associated with our class. Using the syntax `@@var_name` designates a class variable.

```ruby
class Person
  attr_accessor :name
  @@population = 0
  @@zip_code = 98101 # downtown Seattle

  def initialize(name)
    @name = name
    @@population += 1
  end
  
  def self.population
    @@population
  end
  
  def self.zip_code
    @@zip_code
  end
  
  def self.zip_code=(new_zip)
    @@zip_code = new_zip
  end
end
```

We have to create a method on the class to make the class variable accessible. Now we can access the value without creating any people.

```rb
puts "Population: #{Person.population}"
puts

batman = Person.new("Bruce Wayne")
superman = Person.new("Clark Kent")
Person.print_population
puts

# we can access the population and zip code directly
puts "Population: #{Person.population}"
puts "Zip Code: #{Person.zip_code}"
puts

# no one should be allowed to redefine the population
# there is no setter defined for population. this will crash.
# Person.population = 8

# however, the zip code can totally be updated!
Person.zip_code = 98122 # capitol hill

puts Person.print_population
```


If we create a few people, we see the following

```rb
Person.new("John")
Person.new("Jane")
Person.population
#=> 2
```

What about class methods? We can also create a method that belongs to a class.
```ruby
class Person
  attr_accessor :name
  @@population = 0

  def initialize(name)
    @name = name
    @@population += 1
  end

  def self.print_population
    puts "There are #{self.population} people"
  end
end
```

In most cases, inside an instance method, self refers to the object, but when used in the context of a method name, self refers to the *class* itself`.

Also, note that `self` can be used in instance methods to refer to particular *object* in use, i.e. `self.var_name` instead of `@var_name`.


### Private Methods

If we create a class `Person` with a name attribute and use `attr_accessor` to create the getters and setters as follows

```rb
class Person
  attr_accessor :name

  def initialize(name)
    @name = name
  end
end
```

then anyone can read and access `Person#name`.

```rb
person1 = Person.new("John")
person1.name

=> "John"
```

We can change this using the `private` keyword. Everything under the private keyword is private to outside users. Only the instance methods can use the getter and setter.

```rb
class Person
  def initialize(name)
    @name = name
  end

  private

  attr_accessor :name
end
```

We can also add private methods by defining new methods below the `private` keyword

```ruby
class Person

  def initialize(name)
    @name = name
  end

  private

  attr_accessor :name
  
  def make_call
    puts "Calling friends"
  end
end
```

Note that we can create a **public** method that calls a **private method**, because we are within the class.

```ruby
class Person

  def initialize(name)
    @name = name
  end

  def call
    make_call if name
  end

  private
  
  attr_accessor :name
  
  def make_call
    puts "Calling friends"
  end
end
```

### Chainable methods

What if I wanted to create a class that had **chainable** methods calling many methods in one line.

```ruby
class Person
  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello I am #{@name}."
    puts "What is your name?"
    @other = gets.chomp
    puts "Nice to meet you, #{@other}."
  end

  def thank
    puts "Thank you for coming."
  end

  def farewell
    puts "Farewell, #{@other}"
  end
end
```


Trying to do

```ruby
person1 = Person.new("john")
person1.greet.thank.farewell

#=> NoMethodError: undefined method `thank' for nil:NilClass
```

to achieve this we have to return a reference to the object after each method

```ruby
class Person
  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello I am #{@name}."
    puts "What is your name?"
    @other = gets.chomp
    puts "Nice to meet you, #{@other}."
    self
  end

  def thank
    puts "Thank you for coming."
    self
  end

  def farewell
    puts "Farewell, #{@other}"
    self
  end
end
```
