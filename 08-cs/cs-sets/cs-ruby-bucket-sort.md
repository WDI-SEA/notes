# Bucket Sort

Bucket sort is a distribution sort in which we take the original unsorted elements in an array and distribute them into a set of buckets. Each bucket is meant to hold a range of element values. After we have distributed all the elements from the array into the buckets, we sort each bucket and then concatenate them all into a single array again. At the end of the process, the original array will be sorted.

## Algorithm Analysis

In the best and average cases, bucket sort operates at O\(n+k\) time efficiency where `n` is the number of elements in the array and `k` is the number of buckets you create for sorting. Every operation that we do in a bucket sort is actually O\(n\) which is "linear time" but the final concatenation of the buckets can be done in constant time, or O\(k\). As a result, our efficiency for this algorithm is the sum of both of those: O\(n+k\). In the worst case, bucket sort can perform like a quadratic search at O\(n2\).

This worst case can happen when we don't have a very even distribution of the values to be sorted. If we have a bunch very near each other, they will all be sorted into the same bucket. This will increase the time needed to sort to closer to a quadratic. As a result, bucket sort is not a great option when you have a lot of repeats or an uneven range of values.

## Characteristics

* Distribution Sort - puts values into auxilliary data structures
* Not in place - requires additional space and returns a new sorted array
* Stable - preserves original ordering of duplicates

## The Algorithm

* The function takes as parameters the array to be sorted \(`arr`\) and the number of buckets to create \(`k`\). \(Remember that the number of elements in the array/list and the number of buckets determines the efficiency of this algorithm since it is O\(n+k\).\)
* Create a new array of `k` empty buckets \(array of arrays / list of lists\).
* Iterate over the unsorted array to find the maximum value.
* Iterate over that array again to scatter each element into the appropriate bucket.
* Iterate over the buckets array and sort each bucket \(usually we use **insertion sort**\).
* Return all the buckets concatenated in order.

## Calculating the Correct Bucket

This can actually be done mathematically if we know both the number of buckets and the maximum value in our unsorted array. Consider a list of integers:

```python
ints = [19, 28, 61, 32, 17, 59, 48, 4, 10, 74, 39, 69]
```

Our maximum value in here is 74. We don't want too few buckets but we also don't want too many. Having one bucket for each element actually becomes a different kind of sort known as pidgeonhole sort. With 12 values in the list, why don't we choose 6 which will make sorting each bucket extremely easy. Then the formula for calculating the bucket for each unsorted element is:

```python
bucket_index = math.floor((unsorted_value / maximum + 1) * k)
```

> NOTE: As we will see, this works great for integers but will need to be tweaked for other types like floats or strings.

Let's see if we can understand what this is doing. When we divide the unsorted value by the maximum value in our list plus one, we get a fractional value that helps us approximate where it should be placed in our range. Values closer to the max will have a ratio closer to 1 while lower values will have ratios closer to 0. This gives us a kind of measurement of where this value should go in the final sorted list. We take this ratio and multiply it by the number of buckets and then get the floor of the whole thing to find the index of the bucket closest to where that value should end up. Let's see where our values end up:

```text
math.floor((19 / 75) * 6) = 1
math.floor((28 / 75) * 6) = 2
math.floor((61 / 75) * 6) = 4
math.floor((32 / 75) * 6) = 2
math.floor((17 / 75) * 6) = 1
math.floor((59 / 75) * 6) = 4
math.floor((48 / 75) * 6) = 3
math.floor(( 4 / 75) * 6) = 0
math.floor((10 / 75) * 6) = 0
math.floor((74 / 75) * 6) = 5
math.floor((39 / 75) * 6) = 3
math.floor((69 / 75) * 6) = 5
```

```python
#    0         1         2         3         4         5
[ [4, 10], [19, 17], [28, 32], [48, 39], [61, 59], [74, 69] ]
```

Not too shabby! Now all we need to do is sort each bucket and then concatenate them all together and return it.

## Implement it!

Now that you have an understanding of how this works, take a stab at implementing it for sorting a list of integers.

### Bonus:

If you get that working, try changing it to a list of float values between zero and one \(e.g. 0.334, 0.167, 0.834, etc.\). How would you need to modify the bucket index calculation to make it work for a list of fractional float values?

