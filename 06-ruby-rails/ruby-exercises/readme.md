# Ruby Challenges

## Getting Started

* Fork and clone this repository
* Run `bundle install` to install dependencies
  * Run `rubocop` to lint your code
  * Run `ruby lib/file_name.rb` to run your file

## Requirements

Complete each challenge in a separate file.

### Challenge 1 - Calculator

Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

```
What calculation would you like to do? (add, sub, mult, div)
add
What is number 1?
3
What is number 2?
6
Your result is 9
```

### Challenge 2 - Reverse a string

Reverse a string in place. In other words, do not create a new string or use other methods on the string such as `reverse`. The goal of the problem is to use a loop and the string accessors to figure out which values to swap for other values. Below is some sample output.

```
Enter a string:
reverse_me
em_esrever
```

### Challenge 3 - Bank Transactions

Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user. Here is a sample output:

```
Your current balance is
4000
What would you like to do? (deposit, withdraw, check_balance)
deposit
How much would you like to deposit?
1000
Your current balance is 5000
Are you done?
yes
Thank you!
```

### Challenge 4 - Guessing Game

Create a program that asks the user to guess a number between 1 and 100. Once the user guesses a number, the program should say, higher, lower, or tell the user that he got the number correct.  The user should continue to make guesses until he guesses correctly. Also, once the user guesses correctly, the program should print the number of guesses needed to arrive at the correct answer. Below is sample output:

```
Guess a number between 1 and 100
50
The number is lower than 50.  Guess again
25
The number is lower than 25.  Guess again
13
The number is higher than 13.  Guess again
20
The number is lower than 20.  Guess again
17
The number is higher than 17.  Guess again
18
The number is higher than 18.  Guess again
19
You got it in 7 tries
```

---

## Licensing
1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
