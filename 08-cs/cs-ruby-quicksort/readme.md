# Quicksort

The idea of quicksort is to take an array and divide it into partitions. As a result, we get 3 partitions.

1. The bottom partition, which should contain numbers lower than the pivot.
2. The top partition, which should contain numbers higher than the pivot.
3. The pivot (a single element).

**Example**
```
[8, 5, 2, 7, 1, 9, 3, 6, 4]
```

If we choose the last element as the pivot by default (in this case, the number **4**), we need to partition the array like so:

```
  left    pivot      right
[2, 1, 3], [4], [8, 5, 7, 9, 6]
```

In this case, the pivot (number **4**) is considered sorted, and then we call quicksort on the remaining two partitions.

```
left
[2, 1, 3] <= choose 3 as the pivot
[1], [2], [3] <= partitioned
```

Now, the left partition pivot (number **3**) is considered sorted. Since the left and right partitions are single-element arrays, they're sorted as well.

```
  left    pivot       right
[1, 2, 3], [4], [8, 5, 7, 9, 6]
```

```
Right partition
[8, 5, 7, 9, 6] <= choose 6 as the pivot
[5, 6, 7, 9, 8] <= partitioned
       |				<= now we need to partition again (this is the recursive step)
       V
left2       pivot2  right2
[5],         [6],    [7, 9, 8]
```

Now, the right partition pivot (number **6**) is considered sorted. Since left2 is a single-element array, it's considered sorted as well. Now for right2.
```
left2 partition
[7, 9, 8] <= choose 8 as the pivot
[7, 8, 9] <= partitioned

Now left2 is sorted. Final right partition:
[5, 6, 7, 8, 9]

Combining the left partitions and right partitions give us:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
[Another good explanation (with visuals)](http://me.dt.in.th/page/Quicksort/)

## Implementation

Quicksort is one of the more difficult sorts to implement, so a partition function is provided for you. This function partitions a section of an array and returns the pivot. Implement quicksort while meeting the following requirements:

* written in Ruby
* no built-in functions (such as sort!)
* passes testing

## Testing

Test your quicksort algorithm using a shuffled array and compare it to an ordered array.

**Example**
```
test = (1..10).to_a.shuffle
quicksort(test, 0, test.length-1)

if test == (1..10).to_a
	puts 'The sort worked!'
else
	puts 'Noooo, the sort failed!'
end
```
