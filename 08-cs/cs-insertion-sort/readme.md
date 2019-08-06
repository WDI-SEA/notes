# Insertion Sort

The next sort we will be learning is insertion sort. Like bubble sort, it is one of the less efficient sorting algorithms, having a time complexity of O(n<sup>2</sup>). Bubble sort, insertion sort, and another simple one called selection sort make up the family of quadratic sorting algorithms. They are called quadratic because their time complexity is a square of the number of elements, meaning that to sort 10 elements takes around 100 comparisons. The reason for this is the nested loops in these algorithms. Creating nested loops where the entire array is iterated once for every element in the array will always create a O(n<sup>2</sup>) algorithm.

However, insertion sort, in practice, is more efficient than both bubble sort and selection sort. It is for this reason that more complex sorts use insertion sort internally as a step in their sorting process. Since we may find an insertion sort inside some other sorting algorithms, we will show you how it works here.

## Characteristics

* Comparison Sort - compares values and swaps them
* In-place - makes swaps directly in the array that was passed in
* Stable - preserves original ordering of ties

## The Algorithm

Insertion sort works the way we sort a deck of cards in our hands. We start at one end and decide whether we want to sort ascending or descending. We look at the cards that come after the first. If a subsequent card belongs in an earlier place in the deck, we move it down until it is located in the right place. Here is some pseudocode:

1. Create an outer loop that goes from 1 through the end of the array to be sorted. We start at 1 and not 0 because when an element has been swapped all the way to the leftmost side (index 0 in the array) we say that it is sorted for the purposes of the algorithm. Other elements may be moved past it but once an element has stopped being swapped it will never evaluated again.
2. Inside the outer loop, create a variable j and set it equal to i.
3. Create an inner while loop that loops while `j > 0` and the element to the left of j is greater than the one at j. If either `j = 0` (we are at the leftmost edge) or if `array[j - 1] <= array[j]` (we don't need to swap) then the inner loop ends and we go back to the next iteration of the outer loop.
4. Inside the inner loop, swap `array[j]` and `array[j - 1]`.
5. Lastly, inside the inner loop, subtract one from j.

That's it! We start at the second element and swap it with the first if the first is greater. The swapping continues until either we reach the leftmost side of the array or until it finds a number with which it should not swap places. Then we increment i to go to the next element and swap it downward until we get it to the right place. Each successive element will swap downward until it is the right place. At the end of the loops, we will have a sorted array.

## Implement It!

### Further Research Resources

* [Insertion Sort illustrated with Hungarian Dance](https://www.youtube.com/watch?v=ROalU379l3U)
* [Wikipedia - Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)
