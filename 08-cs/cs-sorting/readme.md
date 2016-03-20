# Sorting Algorithms

This week, we've gone over the following sorts:

* Bucket sort
* Bubble sort
* Merge sort
* Quick sort

### Here's some more.
* [15 Sorts in 6 minutes (warning, flashing colors)](https://www.youtube.com/watch?v=kPRA0W1kECg)

## Why we have different sorts

* [Side by Side Comparisons](https://www.youtube.com/watch?v=ZZuD6iUe3Pc)
* [Sorting Algorithm Animations](http://www.sorting-algorithms.com/)

Find out which sort is the fastest for each type of data.

## Other sorting topics

### Stability

*What's the difference between stable and unstable sorts? Why would we want a stable sort?*

Stable sorts are sorts that preserve original order of items, when encountering two items of the same value. A good example is when sorting some people. Let's say there's an array of 4 people, represented by hashes:

```rb
my_people = [
  {name: 'Robert', age: 23},
  {name: 'Riley', age: 35},
  {name: 'Rich', age: 43},
  {name: 'Rich', age: 28}
]
```

Sorted by age:

```rb
my_people = [
  {name: 'Robert', age: 23},
  {name: 'Rich', age: 28},
  {name: 'Riley', age: 35},
  {name: 'Rich', age: 43}
]
```

What if I want to now sort by name? This is where stability comes into play. A stable sort will preserve the orders of the ages.

**Stable Sort**

```rb
my_people = [
  {name: 'Rich', age: 28}, # the two Riches are ordered by age
  {name: 'Rich', age: 43},
  {name: 'Riley', age: 35},
  {name: 'Robert', age: 23}
]
```

An unstable sort may not necessary preserve the orders of the ages.

**Unstable Sort**

```rb
my_people = [
  {name: 'Rich', age: 43}, # the two Riches are not ordered by age
  {name: 'Rich', age: 28},
  {name: 'Riley', age: 35},
  {name: 'Robert', age: 23}
]
```

### Types of sorts

**NOTE:** These are not exclusive definitions (for example, a comparison sort can also be an adaptive sort)

#### Comparison Sorts

Bubble sort, merge sort, and quicksort have all been examples of comparison sorts. Positions in a data structure are changed based on comparing values.

#### Distribution Sorts

Bucket sort is an example of a distribution sort, where values are grouped based on certain attributes.

#### Hybrid Sorts

Since sorts like insertion sort are faster for smaller datasets, some recursive sort algorithms can be implemented as hybrid sorts, utilizing sorts like insertion sort on smaller datasets.
