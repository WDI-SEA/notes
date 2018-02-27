# Intro to Heapsort

## What is a heap?

A heap is a tree that has the "heap" property. There can be either max heaps or min heaps. A max heap has the property that for every parent node, it's key is greater than or equal to the key of its child nodes. In other words, in a max heap, the biggest number is at the top. 

[Max Heap](https://res.cloudinary.com/briezh/image/upload/v1519762182/Max-Heap_eir7zo.png)

A min heap is similar to a max heap, except that the parent's key is less than or equal to the child's key. Therefore in a min heap, the smallest number is at the top (or root) of the tree.

## What is heapsort?

Heapsort uses a heap data structure in order to perform a sort. It's an in-place comparison sort. The code implementation uses 3 functions: Heapsort, BuildHeap, and Heapify. Heapsort is the main/entry function, BuildHeap forms your initial heap, and Heapify is to make a non-heap tree into a heap. An important thing to recognize is that an array can be a representation of a tree. Imagine arr[0] as the root of the tree and arr[1] and arr[2] as the left and right nodes of the root. Then arr[3] and arr[4] would be the left and right nodes of arr[1], and so on. For example, take the max heap pictured above. In an array representation that would look like:

```
arr = [100, 19, 36, 17, 3, 25, 1, 2, 7]
```

Thus, for any given index `i`, its children are:
* left: `2*i + 1`
* right: `2*i + 2`


### Pseudocode

The pseudocode for the algorithm goes like this:
1. Using the given array, build a heap using recursive insertion
2. Iterate to extract the max element in the heap and then reheapify the heap
3. Extracted elements form a sorted subsequence

```
Heapsort(Arr)
    BuildHeap(Arr)
    for i in range Arr size down to 1
        swap(A[1], A[i])
        NewSize = reduce size by one
        Heapify(A, NewSize, 1)

BuildHeap(Arr)
    n = Arr size
    for i in floor(n/2) down to 0
        Heapify(Arr, n, i AKA the RootIndex)

Heapify(A as array, i as int, n as int)
    left = 2i
    right = 2i+1

    if (left <= n) and (A[left] > A[i])
        max = left
    else 
        max = i

    if (right<=n) and (A[right] > A[max])
        max = right

    if (max != i)
        swap(A[i], A[max])
        Heapify(A, max)
```

### Code in Python

For working code in Python, [visit this repl](https://repl.it/@brandiw/HeapSort).

## References
[Pseudocode Source](http://www.algorithmist.com/index.php/Heap_sort)
[Coding Geek Implementation/Explanation](https://www.codingeek.com/algorithms/heap-sort-algorithm-explanation-and-implementation/)
