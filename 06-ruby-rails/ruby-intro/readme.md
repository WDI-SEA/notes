#Ruby Crash Course

##Objectives

* Describe the history of the Ruby language
* Identify fundamentals and concepts of the Ruby langauge
* Utilize different primitive types, control structures, and methods in Ruby

##Humble Origins
Ruby is an object-oriented language suitable for writing day to day scripts as well as full-scale applications. Yukihiro Matsumoto, or "Matz", began work on Ruby back in 1993, because he wanted a language that made him productive while being fun to use. Initially popular in Japan, Ruby has been finding its way into the hearts of programmers all over the world.

* Ruby stylistically conforms to the **snake_case** convention
* The [documentation](http://ruby-doc.org/) is fantastic

Further reading: [The Philosophy of Ruby](http://www.artima.com/intv/ruby.html)

###Yukihiro Matsumoto
![Matz-san](http://image.gihyo.co.jp/assets/images/dev/serial/01/software_designers/0034/0034-01.JPG "Yukihiro Matsumoto")

## Why JavaScript, then Ruby?

While Ruby is a general purpose language that can be used for many purposes, we'll be applying it to a web development framework called Rails. We learned JavaScript first because it's the only language that runs natively in browsers, and we'll be utilizing some JavaScript for our front-end code, while utilizing Ruby for our back-end code.

You'll also find that while Ruby is a functional language, functions cannot be passed into other functions (functions are not first-class citizens). However, its object-oriented capabilities and clean syntax provide different strengths as a language. The widely used Rails framework also provides an opinionated development workflow, which can lead to faster development.

## Comments

In JS, we use line and multiline comments.
```js
// here's a line comment

/* And a multiline
   comment
*/
```

In Ruby, multiline comments exist, but we generally use line comments with hashtags, for readability.
```rb
# here is a line comment

# here is a block
# of comments
# for you to read
```

## Variables

Local variables start with a lowercase letter. No `var` necessary.

```rb
my_variable = 5
puts my_variable
#=> 5
```

##Constants

Mostly, we're able to change what a variable's holding if we so choose – constants are designed for the opposite. Constants are meant to be placeholders that never change.

```ruby
SOME_CONSTANT = "donuts"
#=> "donuts"

SOME_CONSTANT = "awesome"
#=> warning: already initialized constant SOME_CONSTANT
```

Note that if we try to reassign a constant, the reassignment still succeeds! All the constant syntax does is throw an error on reassignment.

## Data Types

### Nothingness
Just as Javascript uses undefined or null, ruby uses `nil`

```rb
my_bank_account = nil
```

### Booleans
A binary representation: either `true` or `false`

```rb
is_operating = true
is_broken = false
```

### Numbers
Datatypes used to represent a number
* Fixnum: `23`
* Bignum: `23238923859348534535`
* Float: `23.23`

### Strings
A primative datatype used to represent a string of characters

#### Methods
```rb
.split
.index
.upcase
.downcase
.sub
.gsub
.capitalize
```

#### Examples
```rb
person = 'instructor'

person.split('')
#=> ["i", "n", "s", "t", "r", "u", "c", "t", "o", "r"]

person.index('tr')
#=> 3

person.upcase
#=> "INSTRUCTOR"

person.downcase
#=> "instructor"

person.sub('r', 'a')
#=> "instauctor"
# note that only the first character is replaced

person.gsub('r', 'a')
#=> "instauctoa"
# note that all character instances are replaced

person.capitalize
#=> "Instructor"

person.reverse
#=> "rotcurtsni"

person.length
#=> 10
```

## Operators

```rb
+
-
/
*
** #exponent
% #modulo

+=
-=
*=
/=
**=

==
!=
!
||
&&
```

Note that Ruby has a `===` operator, but no `!==` operator. In fact, the operator means something different in Ruby. We'll touch on this when we get to ranges. You can use the `.equal?` function as an identity operator.

### Arrays
An indexed arrangement of objects

*several ways to create an array*

```rb
arr = [1,2,3]
#=> [1,2,3]
arr1 = Array.new([4,5,6])
#=> [4,5,6]
arr2 = Array.new(3, true)
#=> [true, true, true]
```

#### Array Methods

```rb
.sort
.reverse
.concat
.length
.push (<<)
.shuffle
.shift
.slice (negative indicies, ranges)
.first
.last
.delete
```
  
### Ranges
A set of values with a beginning and an end

```rb
aRange = (1..10) # includes 10
anotherRange = (1...10) # not including 10
lettersWorkToo = ('a'..'z')
```

*typecasting in action*

```rb
anotherRange.to_a
=> [1,2,3,4,5,6,7,8,9]
```

*Using === to determine if an element is within a range or set*
```rb
anotherRange === 3
#=> true
```

###Symbols
An immutable sequence of characters that represents data stored in a specific memory location. Symbols optimize memory and can help programs run faster when performing comparisons or lookups.

```rb
country = :turkey
food = :turkey

country.object_id == food.object_id
=> true

country = "turkey"
food = "turkey"

country.object_id == food.object_id
=> false
```

###Hashes
A hash consists of unindexed key-value pairs. You may construct a hash in either of the following ways. Each will use symbols.

```ruby
dog = {
  :name => "Hamlet",
  :breed => "Pug",
  :fav_food => "paté"
}
cat = {
  name: "Simba",
  breed: "American Shorthair",
  fav_food: "Prosciutto"
}
dog[:name]
=> "Hamlet"
cat[:fav_food]
=> "Prosciutto"
```

###Mutator methods !
Mutator methods will not just return a value, but change the object they are called on to that value. Adding ! to certain ruby methods will turn them into their mutator method counterparts.

*How to mutate an array*

```rb
arr = [7,4,5]
arr.sort #not a mutator method
=> [4,5,7]
arr
=> [7,4,5]

arr = [7,4,5]
arr.sort! #the '!', aka a 'bang' will mutate the object
=> [4,5,7]
arr
=> [4,5,7]
```

###Typecasting
Typecasting is the act of altering an object's datatype

```rb
.to_i
.to_s
.to_a
.to_f
```

##Code blocks
Sometimes called closures in other languages is a chunk of contained code. Use curly braces, `{ }` for single line blocks and `do ... end` for multiline blocks.

```rb
10.times { puts "Hello" }

x = 0
until x > 10 do
  puts x
  x += 1
end

#count to 10
```

##String Interpolation
Allows one to inlcude a dynamic variable in a string

```rb
team = "Mariners"
puts "Go #{team}!"
=> "Go Mariners!"
```

## Control flow

* Conditionals
```rb
if
elsif
else
unless
```

* Loops
```
until
while
times
for
```
* iterators,
```rb
each
map
select
inject/reduce
```

### Examples

#### If/Else
```rb
course = "wdi"
if course == "uxdi"
  puts "Hello, User Experience Designer!"
elsif course == "fewd"
  puts "Hello, Front-End Developer"
elsif course == "wdi"
  puts "Hello, Immersed Student"
else
  puts "Who are you?"
end
```

#### Inline conditional

```rb
if heroic
  do_something_heroic
end

# is the same as
do_something_heroic if heroic == true

# is the same as
do_something_heroic if heroic
```

#### Loops
```rb
i = 0
while i < 5 do
  puts "i is " + i.to_s
  i += 1
end

# is the same as

i = 0
until i == 5 do
  puts "i is " + i.to_s
  i += 1
end

# is the same as

5.times do |i|
  puts "i is #{i}"
end

# is the same as

for i in (0...5) do
  puts "i is " + i.to_s
end


# Will print out:
# >i is 0
# >i is 1
# >i is 2
# >i is 3
# >i is 4
```

#### Iterating through Arrays
```rb
foods = ["carrots", "kale", "beets"]
foods.each do |vegetable|
  puts "i like #{vegetable}"
end

# is the same as

for veg in ["carrots", "kale", "beets"] do
  puts "i like #{veg}"
end

# Will _each_ print out:
# >i like carrots
# >i like kale
# >i like beets
```

#### Iterating through Hashes
```rb
car = {wheels: 4, doors: 2, seats: 5}
car.each do |key, num|
  puts "my car has #{num} #{key}"
end

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

### In Ruby

* uses `def`
* does not capture scope
* not used as values
* implicitly returns last evaluation
* optional parameters must be specified

#### Examples
```rb
def say_hello
  puts "Hello, World!"
end

say_hello()

# is the same as

def say_hello
  puts "Hello, World!"
end

# note missing parentheses
say_hello
```

In Ruby, leaving the `()` off of a function call is acceptable. Since functions can't be passed as values (i.e., aren't first-class), Ruby knows that we mean to call the function, so it calls it.

#### Parameters (Arguments)
```rb
def say_hello(friend)
  puts "Hello, #{friend}!"
end

say_hello("Tim")

# is the same as

def say_hello(friend)
  puts "Hello, #{friend}!"
end

# note the lack of parentheses
say_hello "Tim"
```

#### Return Values
```rb
def add(num1, num2)
  return num1 + num2
end

sum = add(2, 3)
puts "2 + 3 = #{sum}"

# is the same as

def add(num1, num2)
  # note the lack of explicit return
  num1 + num2
end

sum = add(2, 3)
puts "2 + 3 = #{sum}"
```

Ruby will automatically return the value of the last evaluated expression. This is called having "implicit returns". You are free to have an explicit return statement, but you don't have to.

### Input / Output

You've already seen how `puts` will output information to the screen. What if we want to accept user input? Let's try `gets`.

```rb
puts "Enter your name:"
you = gets

puts "Enter a friend's name:"
friend = gets

puts "Hello, #{friend}. #{you} says hi."

# Outputs
# Enter your name:
# Tim
# Enter a friend's name:
# Bob
# Hello, Bob
# . Tim
#  says hi.
```

That almost works as we want, but `gets` is reading in the newline
character from when we pressed the Enter key. Generally, when reading user input we want to `chomp` the data. (See http://www.ruby-doc.org/docs/Tutorial/part_02/user_input.html)

```rb
puts "Enter your name:"
you = gets.chomp

puts "Enter a friend's name:"
friend = gets.chomp

puts "Hello, #{friend}. #{you} says hi."

# Enter your name:
# Tim
# Enter a friend's name:
# Frank
# Hello, Frank. Tim says hi.
```

Much better. Now the unnecessary newlines are removed, thanks to `chomp`.
