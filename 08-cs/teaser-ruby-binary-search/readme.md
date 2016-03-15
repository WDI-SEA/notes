#Auto guess

We previously created a guessing game app that picked a random number and had you guess what it was until you got it correct.

Now we want to make the game guess the number automatically, in as few guesses as possible without teaching.

You can use your version of the guessing game as a starting point or the one included below.

**Use Ruby**

```rb
the_answer = rand(1..100)
user_guess = nil
tries = 0

puts "Guess a number between 1 and 100"
until user_guess == the_answer
  user_guess = gets.to_i
  tries += 1

  # note that the UFO operator returns -1 if the left side < right side
  # note that the UFO operator returns 1 if the left side > right side
  # note that the UFo operator returns 0 if the left side == right side
  case user_guess <=> the_answer
  when -1
    puts "The number is higher than #{user_guess}. Guess again"
  when 1
    puts "The number is lower than #{user_guess}. Guess again"
  when 0
    puts "You got it in #{tries} tries!"
  end
end
```
