# Binary Search

Binary search is an efficient `O(log(N))` algorithm for finding elements in a sorted array. It's important that the array is sorted. Binary Search doesn't work on unsorted arrays.

## Auto Guess

We previously created a guessing game app that picked a random number and had you guess what it was until you got it correct.

Now we want to make the game guess the number automatically, in as few guesses as possible without teaching.

Binary Search finds items quickly by guessing an array index where an element might be, reading the value at that index, and basing it's next guess on what value it read. If the value at the index was less than the value it's searching for its next guess will be a higher index. It chooses a lower index if the value read was higher than what it is looking for.

## Consider How You Use Phonebooks

Imagine flipping through a phone book to find someone's number. A linear O\(N\) algorithm would start at the beginning of the phone book and read every name on every page until it found the name you're looking for. This is terribly slow!

Instead of reading every single name it's much easier to read one random name and flip far forward or backward depending on how close that name is to the name you're looking for.

This only works because the phone book is sorted by names. Imagine trying to do a reverse look up on a mysterious phone number using a phone book. You'd have to start at the beginning and look at every single entry!

### How Fast is Fast?

Imagine we had an array where every array access took 1 second. No matter what index we read it would take a full second for us to get the value. It would take us a minute to read every item in an item with only 60 items in it.

How long is a trillion seconds?

* 1,000 seconds is equal to almost 17 minutes.
* It would take almost 12 days for a million seconds to elapse
* It takes about 31.7 years for a billion seconds to go by.
* A trillion seconds amounts to no less than 31,709.8 years.

It would take practically 31,709 years to search iteratively through an array with one trillion items.

With binary search it would take only 40 guesses to find the correct index. Binary Search reduced the runtime of searching for something in the trillion-length array from 31,709 years to only 40 seconds!

Binary Search is extremely fast.

![Binary Search](../.gitbook/assets/binary-search.png)

### Implement It

Your task is to implement this algorithm. Algorithms like these are language independent, meaning the language syntax may change but the logical flow is always the same. Binary Search is a recursive function and it runs until it finds the index of the value being searched for or until the portion of the array it is searching contains no elements.

* Function takes four parameters: the array \(`arr`\), the search value \(`val`\), the starting index \(`start`\), and the ending index \(`end`\).
* `start` and `end` are [optional parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) \(for the first call\). Give `start` a default value of 0 and give `end` a default value of `null`.
* Inside your function, you must detect if `end` is `null`. If it is, you need to then set it to `arr.length - 1` so it holds the last index in the array.
* Find the index midway between `start` and `end`. \(Not important if it isn't exactly midway.\)
* Compare the value at the `mid` index to the value \(`val`\) being searched for.
* If it matches, return that index \(`mid`\).
* If the value at `mid` is greater than `val` then recurse on the left half of the array.
  * Call `binarySearch` again with the same `arr` and the same `val` but change the `start` and `end`:
  * For the left half, use the same index for `start` but use `mid - 1` for the `end` value.
* If the value at `mid` is less than `val` then recurse on the right half of the array.
  * Call `binarySearch` again with the same `arr` and `val` but change `start` and  `end`:
  * For the right side, use `mid + 1` for `start` and use the existing index in `end`.
* If ever your `start` index is greater than your `end` index, you are immediately done. Return `-1` to indicate that the value was not found in the array.

You may assume the given array is sorted. Your code must handle the case when the array is empty.

### Thought Experiment

Binary Search is able to return useful information even if the element isn't even in the array.

What happens when an element isn't in a array?

```javascript
var nums = [7, 10, 20, 30, 40, 50, 60]
binarySearch(nums, 15); // returns -1
```

Here's what happens when Binary Search runs:

```javascript
guess = 4    // start guessing at 4
nums[4] = 40 // value is higher
guess = 2    // guess lower
nums[2] = 20 // value is higher
guess = 1    // guess lower
nums[1] = 10 // value is lower
guess = 2    // guess higher.  wait! we already guessed this.
```

It can actually return an index representing where an element _should_ be. Instead of manually returning `-1` we can _almost_ return the index of our last guess. The index of our last guess represents where the element would be if it were in the array. Then, we could manually add the item at exactly the correct index and the array would remain sorted.

If we simply return the index of our last guess how would users of our algorithm tell the difference between when the number was found, and when we're trying to tell them the index of where it should go?

Instead of returning the index return the negative index! Now any positive number that comes back from the binary search represents that the element was found there. Any negative number that comes back from the array means that the element wasn't found, but we can do some math on the result and determine where it _should_ be added.

Wait. What's negative zero? Still just zero.

There's one small problem. The zero-index of arrays complicates the idea that we can simply return the negative index of our last guess. If the algorithm returned zero it would be impossible to tell if it meant it **found** the element at zero, or if it means the element wasn't found and it _should be added_ at element zero.

Instead of returning `-guess` return `-(guess - 1)`. This shifts zero indexes from zero to negative one. And now our algorithm truly fits these rules:

1. `binarySearch(n) >= 0` is the index of the element in the array
2. `binarySearch(n) < 0` means the element wasn't found.

If binary search returns a negative number we can add 1 to it and negate it to determine where a non-found element should be inserted.

```javascript
var index = binarySearch(n);
var insertIndex = undefined;

if (index < 0) {
  insertIndex = -(index + 1);
}
```

