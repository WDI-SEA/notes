# Inheritance in Ruby

## Objectives

* Implement inheritance
* Describe what has been inherited from one class to another
* Compare and contrast inheritance in Ruby with Prototypical inheritance in Javascript
* Utilize inheritance to reduce repetition
* Utilize inheritance to model the world
* Install `pry` using `gem`. Pry is an improved REPL for Ruby that allows for better debugging and lets you work interactively with pre-written scripts through the use of `binding.pry`

#### Quick Review
1. What is a method? What is a class?
2. What is an instance method?
3. Why do we use a class?

## Inheritance

Inheritance is used to indicate that one class will get most or all of its features from a parent class. Inheritance is useful for a couple reasons.

* DRY - Don't Repeat Yourself & reuse code functionality
* Faster implementation time

### Example

```ruby
class Rectangle

  def initialize(l, w)
    @length = l
    @width = w
  end

  def get_area
    @length * @width
  end

  def print_shape
    puts "This is a rectangle"
  end

end

class Square < Rectangle
  def initialize(s)
    super(s, s)
  end

  def print_shape
    puts "This is a rectangle and a square"
  end
end
```

Note from the example above...

* In order to inherit from a class, we use the `<` keyword and specify the class we want to inherit from
* In order to correctly inherit from `Square`, we need to call the parent class's `initialize` method. We can do so by using the `super` method.
  * If we forget to do this, class and instance variables in the parent will not be initialized
  * When you invoke the `super` method with arguments, Ruby sends a message to the parent of the current object, asking it to invoke a method of the same name as the method invoking super.
* Once we inherit from another class, we can access methods and properties from the parent. In the case of this `Square` class, we also overrode the functionality of the `print_shape` method.

### Binding to an interactive console with `pry`

You can use pry to halt the execution of your program and start an interactive console. This is a great debugging tool.

Create a few rectangles and a square at the end of your file. Write `pry.binding` to stop the program after the shapes
are created. You must import this `pry` library by writing `require.pry` at the top of your program.

Install pry by running `gem install pry` in your terminal

```ruby
require 'pry'

r1 = Rectangle.new(3, 4)
r2 = Rectangle.new(4, 7)
s1 = Square.new(3)

# halt the program just after the shapes are created
pry.binding
```

Now you can type expressions into the console and have them evaluated. Your console will look like this. Typing `r1` and `r2`
shows the type of objects that exist in those variables. Typing `r1.get_area` executes the function and prints the
result. 

```ruby
[1] pry(main)> r1
=> #<Rectangle:0x007fe85311f6f0 @height=4, @width=3>
[2] pry(main)> r2
=> #<Rectangle:0x007fe85311f6c8 @height=7, @width=4>
[3] pry(main)> r1.get_area
=> 12
```
Having access to a console like this is a great way to explore ruby with new pieces of code to make sure they work.
Type things into the interactive console to figure out how you could calculate the area of a circle: Pi r squared.

Here's an example of me using the interactive console to try to find out how ruby's math module works, and where the
value of Pi lives within it. Notice that it's totally ok to cause errors! The interactive console just prompts you
to try again.

```
# is it called MATH?
[10] pry(main)> MATH
NameError: uninitialized constant MATH
from (pry):10:in `<main>'

# is it called math?
[11] pry(main)> math
NameError: undefined local variable or method `math' for main:Object
from (pry):11:in `<main>'

# finally found the proper Math object
[12] pry(main)> Math
=> Math

# where the heck does Pi exist?
[13] pry(main)> Math.pi
NoMethodError: undefined method `pi' for Math:Module
from (pry):13:in `<main>'

[14] pry(main)> Math.PI
NoMethodError: undefined method `PI' for Math:Module
from (pry):14:in `<main>'

[15] pry(main)> Math.Pi
NoMethodError: undefined method `Pi' for Math:Module
from (pry):15:in `<main>'

# hmm, I remember seeing this strange syntax.. there Pi is!!
[16] pry(main)> Math::PI
=> 3.141592653589793
```


### A Guide through Animals

```ruby
class Animal

  def initialize(kind)
    @kind = kind
    @state = "awake"
  end

  def eat(food)
    if @state == "awake"
      puts "NOM-nom!!"
      puts "(#{kind} has eaten #{food})"
    else
      puts "SLEEPING"
    end
    self
  end

  def sleep
    @state = "sleeping"
    self
  end

  def wake
    @state = "awake"
    self
  end
end

class Person < Animal
  def initialize(age, gender, name)
    super("Human")
    @age = age
    @gender = gender
    @name = name
  end
end
```

#### Single Inheritance vs Multiple Inheritance
* In Ruby, a class can only inherit from a single other class. It **cannot** inherit from multiple classes.
  * Think about it. What are some benefits and disadvantages to single & multiple inheritance?

#### Exercise
Create a Mammal class, Cat class, and Dog class. Have Cat and Dog inherit from Mammal. Include some attributes for each class and a method for mammal.

Make cats fall asleep when they're fed tuna. Make dogs fall asleep when they're fed a bone. 
