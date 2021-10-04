# Merge Sort

We are now moving away from the slower quadratic sort algorithms and are going to take a look at two of the faster sorts. The first is Merge Sort.

Merge Sort operates on the principle that an array of 1 or 0 elements is inherently sorted. The first step is to recursively divide the original array into smaller and smaller halves until you end up comparing an array of 1 to an array of either 0 or 1, which is a very easy comparison to make. At that point, you concatenate the values into a new array in the proper sorted order. This now-sorted array is compared with the next now-sorted array and those are merged into a single sorted array. This process continues until the orignal halves are re-joined in the sorted order.

[Watch Merge Sort illustrated by Germanic folk dance](https://www.youtube.com/watch?v=XaqR3G_NVoo)

## Algorithm Analysis

The time complexity of merge sort is O\(n log\(n\)\). O\(n log\(n\)\) time is faster than O\(n2\) or quadratic sorts, but it is not as fast O\(n\) or linear sorts. Linear time on sorts \(needing only ~1 comparison per element\) is rare and is usually only possible if the dataset to be sorted is already very close to sorted. As such, O\(n log\(n\)\) sorts are usually the best ones we can use.

Merge sort does not produce an in-place sort. Therefore, there is some additional space requirement for running this sort. We express the space complexity as O\(n\) or linear space complexity. This means you need one additional place in memory for every element in the array, \(but not more than one.\) The only thing better than linear time or space complexity is **constant time or space complexity** which means that the time or space requirements for it never change regardless of how much data needs to be sorted. Any sort that does an in-place sort is said to have constant space complexity since it needs no additional space.

## Characteristics

* Comparison Sort - compares values and swaps them
* NOT In-place - allocates additional memory for sorting items
* Stable - preserves original ordering of ties

## The Algorithm

Merge sort actually involves two functions: one to split the array in successive halves until you are dealing with single or no-element arrays, and the other to merge them back together in sorted order. Typically, we name the first one `merge_sort` and the second one just `merge`.

Let's start with `merge_sort` since that it the one that starts the process:

1. The `merge_sort` function takes an array as a parameter and calls itself recursively to split the array so we need to define a base case. Above, we learned that an array of 1 or 0 elements is inherently sorted so those are our base cases. We simply return the array if the length is 1 or less.
2. If the length is longer, we find the middle index of the array and split the array in equal halves \(or nearly equal halves\).
3. We then call `merge_sort` on each side, saving the array that is returned form each side.
4. Finally we call `merge` passing in the now-sorted left and right arrays.

The `merge` function takes a `left` and a `right` parameter that are the arrays to merge. It is also called recursively so we must identify base cases. This function is meant to take two sorted arrays, merge them together into one sorted array, and return that array. So what are the cases where we automatically know what to return. Well, we know that the base cases from the `merge_sort` function operate on the principle that an array of 0 or 1 element is sorted. With that being the case, if either array is empty, simply return the other one. Obviously, the result of merging two sorted arrays, where one contains nothing, is the only array that contains anything. This logic works for empty arrays, too, since sorting two empty arrays together always will just be an empty array. With that in mind...

1. If the right array is empty, return the left array
2. If the left array is empty, return the right array
3. Else, get the first value from both arrays \(should be the least value\) and compare them:
4. If left is smaller than right, remove that element from the left array and store it in a `smallestNumber` variable. Else, remove and store the first element from the right array.
5. Call `merge` again, passing in the arrays in their new state \(one of them just had an element removed\). Store the resulting sorted array in a variable.
6. Finally, add the smallest number to the first position in the sorted array and return it.

Between step 5 and 6 is some magic. Each time we call `merge` recursively, we are removing the smallest element from one of the arrays. Eventually, this will cause one of the arrays to be empty. But at this point, we know the smallest number because we saved it. We simply insert it into the final sorted array to return at position 0 and it will be in its correct place.

## Implement It!

### Further Research Resources

* [MergeSort on TurtorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)
* [MergeSort on Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)

