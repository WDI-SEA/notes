# Binary Search

Binary search is an efficient O(log(N)) algorithm for finding elements in
a sorted array. It's important that the list is sorted. Binary Search doesn't
work on unsortedd arrays.

## Auto Guess
We previously created a guessing game app that picked a random number and had you
guess what it was until you got it correct.

Now we want to make the game guess the number automatically, in as few guesses as
possible without teaching.

Binary Search finds items quickly by guessing a list index where an element
might be, reading the value at that index, and basing it's next guess on what
value it read. If the value at the index was less than the value it's searching
for its next guess will be a higher index. It chooses a lower index if the value
read was higher than what it is looking for.

## Consider How You Use Phonebooks

Imagine flipping through a phone book to find someone's number. A linear O(N) algorithm
would start at the beginning of the phone book and read every name on every page until
it found the name you're looking for. This is terribly slow!

Instead of reading every single name it's much easier to read one random name
and flip far forward or backward depending on how close that name is to the name
you're looking for.

This only works because the phone book is sorted by names.
Imagine trying to do a reverse look up on a mysterious phone number using a
phone book. You'd have to start at the beginning and look at every single entry!

### How Fast is Fast?

Imagine we had an array where every array access took 1 second. No matter what index
we read it would take a full second for us to get the value. It would take us a minute
to read every item in an item with only 60 items in it.

How long is a trillion seconds?

1,000 seconds is equal to almost 17 minutes.
It would take almost 12 days for a million seconds to elapse
It takes about 31.7 years for a billion seconds to go by.
A trillion seconds amounts to no less than 31,709.8 years.

It would take practically 31,709 years to search iteratively through a list with
one trillion items.

With binary search it would take only 40 guesses to find the correct index.
Binary Search reduced the runtime of searching for something in the trillion-length
array from 31,709 years to only 40 seconds!

Binary Search is extremely fast.

### Implement It

Try to implement your own version of binary search. Here's a description of the
algorithm to help get you started:

1. set up variables `min`, `max` and `guess` to keep track of the range of
   indexes you're currently searching through.
2. set `guess` equal to `(min + max / 2)` and round it
3. read the value of the array at the index of `guess`
4. if the value read is higher than `n` then adjust `max = guess - 1`
5. if the value read is lower than `n` then adjust `min = guess + 1`
6. repeat steps 2 through 5 until `n` is found.
7. return `guess` as the index of n

You may assume the given list is sorted. Your code must handle the case when
the list is empty.

```js
// search for the index n inside of list
// return the index of n
// return -1 if it doesn't exist
function binarySearch(list, n) {

}
```
