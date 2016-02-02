#Merge Sort Challenge

All of these components must be done in **Ruby**

##Part 1 - Create Merge

First create a method called `merge` that can combine two sorted arrays and keep them in sorted order. We did this in JavaScript, so feel free to look back at that problem.

**Example**

```rb
# input arrays
a1 = [2,4,6,8]
a2 = [1,3,5,7]

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
