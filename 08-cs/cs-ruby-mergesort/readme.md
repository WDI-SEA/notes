#Merge Sort Challenge

All of these components must be done in **Ruby**

##What is Merge Sort?

Merge sort is a sorting algorithm that's **recursive** (the function calls itself) and uses a **merge** function to combine two sorted arrays. But wait, if we have an array like this...

```
my_arr = [5, 3, 7, 2]
```

...how do we get two sorted arrays out of that? The key is **recursion**, which we'll use to obtain a base case.

Merge sort works by splitting the array in half over and over again, until we're left with single-element arrays. By definition, an array with a single element is sorted, so we can call **merge** on two arrays with one element each. Here's a diagram of how this may occur.

![Merge Sort Diagram](http://shawnjanas.com/wp-content/uploads/2011/06/mergesort.jpg)

An implementation of merge sort should split an array in half recursively, until we're left with single-element arrays. Then, we can start merging them back until the array is finally sorted.

Let's try to implement this, but one step at a time.

##Part 1 - Create Merge

First create a method called `merge` that can combine two sorted arrays and keep them in sorted order. We did this in JavaScript previously, so feel free to look back at that problem.

**Example**

```rb
# input arrays
a1 = [2, 4, 6, 8]
a2 = [1, 3, 5, 7]

a3 = merge(a1, a2)
# a3 is now [1, 2, 3, 4, 5, 6, 7, 8]
```

You should be able to accomplish this with only one trip through the arrays. AKA O(n) time.

##Part 2 - Create Merge Sort

Create a method called `merge_sort` sorts an array by recursively splitting it in half until you are down to one element (base case). Then, use merge to merge all of the 1 element arrays, which will result in a sorted array because the merge function re-assembles them in sorted order.

* You cannot use any of the built-in sort methods.
* The original array should not be modified

**Example**

```rb
#random shuffled array 0 - 10
a = (0..10).to_a.shuffle

#sort using your new method
b = merge_sort(a)

puts a
# unsorted: [10, 4, 7, 3, 8, 9, 2, 1, 6, 5, 0]
# (unsorted results may vary)

puts b
# sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

##Testing

Once you have it working with the simple 0-10 array, try it with some of these other inputs.

```rb
#contains duplicates
a = [5, 8, 2, 5, 3, 5, 1, 7, 8, 5, 6, 5, 1]

#empty array
a = []

#smallest data set
a = [1]

#larger array
a = (0..100000).to_a.shuffle
```

##Resources

If you need help getting started with the idea of merge sort, check out the following resources:

* [Khan Academy: Merge Sort Overview](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)
* [Merge Sort Pseudocode and Visualization](http://www.sorting-algorithms.com/merge-sort)
