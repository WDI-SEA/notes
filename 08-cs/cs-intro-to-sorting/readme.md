# Introduction to Sorting Algorithms

## Objectives

* Describe the difference between a stable and unstable sort
* Describe the difference between a comparison sort and a distribution sort
* Describe what an in-place sort is 
* Name a few common sorting algorithms and...
    * Describe the time complexity
    * Describe the space complexity
    * Tell whether it is a stable sort or not
    * Describe what kind of mechanism the algorithm uses to perform the sort (i.e., comparison, distribution, or hybrid)

## What is a sorting algorithm?

A sorting algorithm takes an unordered collection and gives you an ordered collection. Most commonly, this means numerical order or alphabetical order.

## How many sorting algorithms could there really be?

You'd be surprised. Even a quick glance at your [Big O cheatsheet](http://bigocheatsheet.com/) tells you about bubble sort, merge sort, quick sort, heap sort, radix sort, cube sort, bucket sort, shell sort, tree sort, insertion sort, selection sort, and counting sort. And those are just the more common ones! Check [wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm) for even more sorts.

## Can't you just tell me which one is the best and teach me that one?

Well, yes and no. While there are a few choice sorts you should get very familiar with, there isn't just one answer for which one is the "best" because different sorts are good at different things. Based on your needs for a specific situation, you may want to consider time complexity, space complexity, whether the sort is stable or not, and what kind of mechanism that the algorithm uses to sort.

## Your first sort

### Group Activity

Before we get into any code, let's try sorting a deck of cards by hand. 

With a partner, acquire a set of playing cards. Assign one person to move cards and one person to be in charge of comparisons. 

The card person should lay the cards out in a line on the table. The card person's goal is to sort the cards. Starting at the beginning of the list, for the first two cards, ask the comparison person whether they should swap the two cards or not. Continue this process for the next two cards, and so on until the end of the line. Start over at the beginning when you're done. Keep doing this process until you make a pass through of your line of cards and make zero swaps. Congratulations, you have a sorted deck of cards!

Comparison person: `Always answer ties with "don't swap"` - we'll talk about why that's important in a moment.

Typically, you might have your chosen card order be numerical (as it is in poker), but feel free to pick whatever variation you would like. For example - what if aces were always low? How about reverse order? Or what about using pinochle ordering - [9, J, Q, K, 10, A]?

Swap roles, shuffle your deck, and repeat the process.

### After you're done with the activity

When you're finished having each person sort the cards at least once, discuss with your partner your thoughts on the following questions:

    1. How fast was this sort? Fast, slow, medium?
    2. Did you require any extra space besides the space that the cards were originally laid out in?
    3. What effect did it have on the end result that you did not swap "ties" (e.g., a 5 of hearts and a 5 of diamonds)?
    4. How fast or slow would it be to sort cards that start out already in order?
    5. How fast or slow would it be to sort cards that start out in completely reversed order?
    6. Hypothetically, if you wanted to sort by suits (e.g., clubs < diams < hearts < spades), and then by card value, how would your swap/comparison logic change?
    7. Given your answers to the previous questions, hazard a guess at what this sort's stats are:
        * Best case time complexity (Big Ω)
        * Worst case time complexity (Big O)
        * Space complexity? (Big O)
        * Is this a stable or unstable sort?

The sort you performed is called "Bubble sort". Perhaps you were able to see why in a visual way when you were sorting your cards. For example, if you had a face card at the front of the deck then it sort of `bubbled` up to the place it was supposed to be.

## Sorting Types

The two basic types of sorts are comparison sorts and distribution sorts. 

A *comparison sort* is a sort that compares values to determine what their place is in the final list. An example of a comparison sort would be bubble sort, which compares two items and swaps them depending on the outcome of the comparison. Usually this comparison will be numerical or alphabetical order, but as you may have noted, you can define the comparison however you'd like.

`"A comparison sort is a type of sorting algorithm that only reads the list elements through a single abstract comparison operation (often a "less than or equal to" operator or a three-way comparison) that determines which of two elements should occur first in the final sorted list."`

- [Wikipedia](https://en.wikipedia.org/wiki/Comparison_sort)

A *distribution sort* is a sort that groups together certain items based on their properties. We'll see an example of this later on with bucket sort, or variations of bucket sort such as radix sort.

`"Distribution sort refers to any sorting algorithm where data are distributed from their input to multiple intermediate structures which are then gathered and placed on the output."`

- [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Distribution_sort)

A combination of both of these methods may be used, and this would be known as a *hybrid sort*. An example would be Timsort, which combines merge sort, insertion sort, and other logic (including binary search).

## Sorting Mechanisms

This isn't really an official term, but often you may hear sorts described in greater detail. For example, yes, bubble sort is a comparison sort, but there are lots and lots of comparison sorts. More likely, you might describe the sorting mechanism as 'swapping'. Other sorts you may hear described as 'inserting', 'merging'

## Stable vs. Non-Stable

![Stability](https://infogalactic.com/w/images/thumb/8/82/Sorting_stability_playing_cards.svg/300px-Sorting_stability_playing_cards.svg.png)

A stable sort preserves the ordering of "ties", meaning that if we started out with say a 5&diams; in position 2 and a 5&spades; in position 10, then the 5&diams; would be first and the 5&spades; would be second in our final result.

## Time Complexity

People care a lot about the time complexity of sorting, to the point that they study the best, worst, and average time complexity of each algorithm. You may have noticed that in an ideal scenario, (already sorted or nearly sorted) bubble sort wasn't half bad, but on average, it was really slow. The actual stats for bubble sort are O(n) for best case and O(n<sup>2</sup>) for the worst case. For this reason, sometimes it is good to consider what sort of data you will be usually sorting and what kind of case that would be - best, worst, or average.

## Space Complexity

You may have heard people describe a sort as an "in-place" sort. This means that instead of creating a whole new array to store our data, we can sort simply by moving things around in the existing array. For example - our bubble sort didn't require an

## Okay, where's the cheatsheet?

| Sort | Best Case | Worst Case | Space | Stable | Mechanism | Notes |
| -----|-----------|------------|-------|--------|-----------|-------|
| Bubble Sort | Ω(n) | O(n<sup>2</sup>) | O(1) | Yes | Comparison | Easiest to understand; uses swaps |
| Selection Sort | Ω(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1) | Yes | Comparison | - |
| Insertion Sort | Ω(n<sup>2</sup>) | O(n<sup>2</sup>) | O(n)* | Yes | Comparison | In-place version exists; Uses insertions |
| Bucket Sort | Ω(n+k) | O(n<sup>2</sup>) | O(n+k) | Yes | Distribution | - |
| Radix Sort | Ω(nk) | O(nk) | O(n+k) | Yes | Distribution | Variation of bucket sort; in place versions exist but are not stable | 
| Merge Sort | Ω(n log(n)) | O(n log(n)) | O(n)* | Yes | Comparison | Divide and conquer, uses merges, *in-place version exists |
| Quick Sort | Ω(n log(n)) | O(n log(n)) | O(log(n)) | No | Comparison | Stable versions exist; uses partitioning |
| Heap Sort | Ω(n log(n)) | O(n log(n)) | O(1) | No | Comparison | In-place, but not stable. Like improved selection sort |

#### Notes about table
* Many sorts such as merge sort or insertion sort have an in-place version of the algorithm, however, these solutions may be more complex to implement or have different time complexities than the basic algorithm
* Quick sort has stable implementations available, however the time and space complexity of this alteration of the algorithm is different.
* Quick sort performs worst on data sets with few unique values. An implementation called [Quick3](https://www.toptal.com/developers/sorting-algorithms/quick-sort-3-way) (because it has 3-way partitions instead of 2-way) solves this issue.

### Additional Activities

Get back into your groups of two from earlier and layout your shuffled deck of cards once more. 

#### 1. Selection sort

This time, you're only going to make a swap if your smaller number will be in its final resting place. Thus, you should go through the array and find the lowest number and swap it with the first card. Then do the same thing with the second card, and so on until you're finished.

After you're done, add `Selection Sort` to the table above with your best guesses about what its stats are based on your experience.

#### 2. Insertion sort

You and your partner each have your own table. Start with the cards in random order on one person's table. That person takes one card from the front of the deck and then hands it to the second person. The second person organizes the card on their own table, placing each successive card in order as they come. To do this, compare the new card received to every card in on the new table until you find where it fits.

After you're done, add `Insertion Sort` to the table and guess what the stats are for this sort based on your experience.


